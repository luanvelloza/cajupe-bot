import re
import shutil
from pathlib import Path

class BillingDocumentOrganizer():
    """
    Organizes XML and PDF documents into NF, BOLETO and XML subfolders,
    renaming each file to its document number only.
    """

    def _ask_folder_path(self, message):
            """
                Prompts the user for the folder path and validates the address.
    
                Output:
                    - A string containing the variable's address if the path is valid.
                    - An empty string if the user chooses to exit the system.
            """
    
            while True:
                folder_path = input(message)
                if folder_path == "2" or folder_path == "":
                    print("Encerrando o processo")
                    return ""
                
                if Path(folder_path).exists():
                    return Path(folder_path)
                
                print("Endereço de pasta inválido! Por favor, tente novamente ou digite dois para encerrar o processo.")

    def _create_destination_folder(self, origin_folder):
        folders = {
            "nf_folder":     origin_folder / "NF",
            "bill_folder":   origin_folder / "BOLETO",
            "xml_folder":    origin_folder / "XML",
        }
        for folder in folders.values():
            folder.mkdir(exist_ok=True)
        return folders


    def _check_incomplete_documents(self, registry):
        """Lists missing documents (NF/BOLETO/XML) with reference to existing files."""
        types = ("NF", "BOLETO", "XML")
        missing = []  # (doc_type, document_number, sibling_names)

        for document_number, docs in registry.items():
            # Real filenames (ignore _DUP keys, if any)
            existing_names = [v for k, v in docs.items() if not k.endswith("_DUP")]
            reference = ", ".join(sorted(existing_names)) if existing_names else "-"

            for doc_type in types:
                if doc_type not in docs:
                    missing.append((doc_type, document_number, reference))

        if not missing:
            print("\n✅ Todos os documentos possuem NF, Boleto e XML.")
            return

        print("\n" + "=" * 80)
        print("⚠️  DOCUMENTOS FALTANTES:")
        print("=" * 80)
        print(f"{'Tipo':<7} | {'Número':<8} | {'Nome original (referência)':<40} | {'Status':<10}")
        print("-" * 80)

        for doc_type, document_number, reference in sorted(missing, key=lambda x: (x[1], x[0])):
            print(f"{doc_type:<7} | {document_number:<8} | {reference:<40} | {'FALTANDO':<10}")

        print("=" * 80)

        # Summary by type
        print("\nResumo do que falta:")
        for doc_type in types:
            count = sum(1 for t, _, _ in missing if t == doc_type)
            if count:
                print(f"   {doc_type}: {count} documento(s) sem {doc_type}")


    def run_bot(self):
        # 1. Ask for the origin folder
        origin_folder = self._ask_folder_path("Informe o endereço da pasta que contenha os arquivos (Sem Aspas): ")
        if origin_folder is None or origin_folder == "":
            return

        # 2. List all XML and PDF files in the folder (ignore subfolders)
        files = [
            f for f in origin_folder.iterdir()
            if f.is_file() and f.suffix.lower() in (".xml", ".pdf")
            ]
    
        if not files:
            print("⚠️  Nenhum arquivo XML ou PDF encontrado na pasta.")
            return

        # 3. Create destination folders and subfolders
        destination_folder = self._create_destination_folder(origin_folder)
    
        counter = {"NF": 0, "BOLETO": 0, "XML": 0, "IGNORADO": 0}
        registry = {} # {document_number: {"NF": filename, "BOLETO": filename, "XML": filename}}

        for file in files:
            name = file.name
            name_upper = name.upper()
            
            # 4. Identify the document type
            # Extract the document number (first number after "DOCUMENTO_")
            doc_number_match = re.search(r"DOCUMENTO_(\d+)", name_upper)
            if not doc_number_match:
                # If "DOCUMENTO_<number>" is not found, fall back to the first number in the name
                doc_number_match = re.search(r"(\d+)", name_upper)
            
            if not doc_number_match:
                print(f"⚠️  Não foi possível extrair número do arquivo: {name}")
                counter["IGNORADO"] += 1
                continue
            
            document_number = doc_number_match.group(1)
            
            # Decide the destination based on the document type
            if file.suffix.lower() == ".xml":
                target_folder = destination_folder["xml_folder"]
                new_filename = f"{document_number}.xml"
                doc_type = "XML"
            elif "BOLETO" in name_upper:
                target_folder = destination_folder["bill_folder"]
                new_filename = f"{document_number}.pdf"
                doc_type = "BOLETO"
            elif "DANFSE" in name_upper or "NF" in name_upper or "NFSE" in name_upper:
                target_folder = destination_folder["nf_folder"]
                new_filename = f"{document_number}.pdf"
                doc_type = "NF"
            else:
                # Unidentified PDF — treat as NF by default
                target_folder = destination_folder["nf_folder"]
                new_filename = f"{document_number}.pdf"
                doc_type = "NF"
                print(f"ℹ️  PDF sem identificação clara, movido para NF: {name}")

            # Build the registry entry for each processed file.
            registry.setdefault(document_number, {})
            if doc_type in registry[document_number]:
                # Duplicate: this number already has a file of this type.
                registry[document_number][doc_type + "_DUP"] = name
            else:
                registry[document_number][doc_type] = name
            
            target_path = target_folder / new_filename
            
            # Avoid overwriting existing files
            duplicate_counter = 1
            while target_path.exists():
                target_path = target_folder / f"{Path(new_filename).stem}_{duplicate_counter}{Path(new_filename).suffix}"
                duplicate_counter += 1
            
            try:
                shutil.move(str(file), str(target_path))
                counter[doc_type] += 1
            except Exception as e:
                print(f"❌ Erro ao mover {name}: {e}")
                counter["IGNORADO"] += 1

        self._check_incomplete_documents(registry)

        # 5. Summary
        print("\n" + "=" * 50)
        print("📊 RESUMO:")
        print(f"   NF:       {counter['NF']} arquivo(s)")
        print(f"   BOLETO:   {counter['BOLETO']} arquivo(s)")
        print(f"   XML:      {counter['XML']} arquivo(s)")
        if counter["IGNORADO"]:
            print(f"   Ignorados: {counter['IGNORADO']} arquivo(s)")
        print("=" * 50)
    