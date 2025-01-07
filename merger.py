from PyPDF2 import PdfMerger, PdfReader, PdfWriter
import os

def clean_pdf(input_path, output_path):
    """
    Create a clean copy of the PDF without named destinations
    """
    reader = PdfReader(input_path)
    writer = PdfWriter()
    
    # Copy only the first page without named destinations
    writer.add_page(reader.pages[0])
    
    with open(output_path, 'wb') as output_file:
        writer.write(output_file)

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
    
    # Create temporary directory for cleaned PDFs
    temp_dir = os.path.join(input_folder, "temp_cleaned")
    os.makedirs(temp_dir, exist_ok=True)
    
    # Create PDF merger object
    merger = PdfMerger()
    
    # Add each PDF to the merger
    for pdf_file in pdf_files:
        try:
            input_path = os.path.join(input_folder, pdf_file)
            temp_path = os.path.join(temp_dir, f"cleaned_{pdf_file}")
            
            print(f"Cleaning: {pdf_file}")
            clean_pdf(input_path, temp_path)
            
            print(f"Adding first page of: {pdf_file}")
            merger.append(temp_path)
            
            # Clean up temporary file
            os.remove(temp_path)
            
        except Exception as e:
            print(f"Warning: Could not process {pdf_file}: {str(e)}")
            continue
    
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Write the merged PDF
    with open(output_path, 'wb') as output_file:
        merger.write(output_file)
    
    # Remove temporary directory
    try:
        os.rmdir(temp_dir)
    except:
        print(f"Warning: Could not remove temporary directory: {temp_dir}")
    
    print(f"PDFs merged successfully to: {output_path}")
    return True

def main():
    # Specify input and output paths
    input_folder = "./input/temp_cleaned"  # Folder containing PDFs to merge
    output_path = "./pdf/merged_output.pdf"
    
    try:
        merge_pdfs_in_folder(input_folder, output_path)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()