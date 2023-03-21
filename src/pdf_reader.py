import tabula


file_path = "teste.pdf"

df = tabula.read_pdf(file_path, pages='all', guess=True, multiple_tables= True, stream=True, java_options="-Dfile.encoding=UTF8")[0]

tabula.convert_into(file_path, "teste.csv", output_format="csv", pages='all')

print(df)
