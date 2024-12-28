from PyPDF2 import PdfMerger
import os

def merge_pdfs_in_folder(input_folder, output_path):
    """
    Merge all PDFs in the specified folder into a single PDF
    """
    # Get all PDF files from the folder
    pdf_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.pdf')]
    
    if not pdf_files:
        print(f"No PDF files found in {input_folder}")
        return False
    
    print(f"Found {len(pdf_files)} PDF files to merge")
    
    # Create PDF merger object
    merger = PdfMerger()
    
    # Add each PDF to the merger
    for pdf_file in pdf_files:
        file_path = os.path.join(input_folder, pdf_file)
        print(f"Adding: {pdf_file}")
        merger.append(file_path)
    
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Write the merged PDF
    with open(output_path, 'wb') as output_file:
        merger.write(output_file)
    
    print(f"PDFs merged successfully to: {output_path}")
    return True

def main():
    # Specify input and output paths
    input_folder = "./input"  # Folder containing PDFs to merge
    output_path = "./pdf/merged_output.pdf"
    
    try:
        merge_pdfs_in_folder(input_folder, output_path)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()