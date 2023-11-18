import streamlit as st
import streamlit.components.v1 as stc
from PIL import Image
img= Image.open('E:\Somaiya Notes\Python\inv1.jpg')
st.image(img, width=200)
st.title('Invoice Amount Displayer')
st.markdown('''
Here you can extract the Total Amount Data any kind of invoice!
''')

from io import StringIO
import typing
from borb.pdf.document import Document
from borb.pdf.pdf import PDF
from borb.toolkit.text.simple_text_extraction import SimpleTextExtraction

st.header("Document files")
pdf_file = st.text_input("Enter path to pdf file")
ms=st.button("Get Amount")

@st.cache
def main(pdf_file):
    f= open("file.txt","w")
    p: typing.Optional[Document]=None
    s: SimpleTextExtraction= SimpleTextExtraction()
    with open(pdf_file, "rb") as pdf_in_handle:
        p=PDF.loads(pdf_in_handle,[s])
       
        
        assert p is not None
        f.write(s.get_text_for_page(0))
        
        f.close()
        with open('file.txt') as f:
            contents= f.read()
            import re
            print(contents)
            result= re.findall(r"[-+]?\d*\.\d+", contents)
            
            Total_amount= max(result,key=lambda x:float(x))
            print(Total_amount)
            return Total_amount
if ms==True:
    Total_amount=main(pdf_file)
    st.write(Total_amount)
