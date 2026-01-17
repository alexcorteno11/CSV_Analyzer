# I import the libraries that i used to create this program
import streamlit as st  # Streamlit for visualizing the structure in the web
import pandas as pd  # Pandas for Data Analysis
import seaborn as sns
import matplotlib.pyplot as plt  # Seaborn and Matplotlib to create graphics
from fpdf import FPDF  # FPDF to let the user save his  analysed data as PDF

# Title that is shown on the app
st.title('Analizador de CSV')

# The user uploads the file to analyze
archivo = st.file_uploader('Sube tu archivo CSV', type='csv')

# Only if the user uploads a file then we proceed with the analysis
if archivo is not None:
    # we read the document as a dataframe with pandas
    df = pd.read_csv(archivo)

    # We show a preview of the file so that the user can confirm it is the right one
    st.subheader(' Vista Previa del Archivo ')
    st.write(df.head())

    # We show basic information about the file, such as number of rows and columns
    st.subheader('Informacion General')
    st.write(f'Filas: {df.shape[0]}, Columnas : {df.shape[1]}')
    st.write('Columnas disponibles : ', list(df.columns))

    # We open a selectbox to let the user decide which column to analyse
    columna = st.selectbox('Selecciona una columna para analizar', df.columns)

    # if the user selects a column, then we proceed with the analysis
    if columna:
        st.subheader(f'Analisis de columna : {columna}')

        # We verify with pandas function if the analysed column is numeric or not
        if pd.api.types.is_numeric_dtype(df[columna]):

            # We show basic statistics information
            st.write(f'Promedio : {df[columna].mean(): .2f}')
            st.write(f'Maximo : {df[columna].max()}')
            st.write(f'Minimo : {df[columna].min()}')

            # We create a figure and an axis with matplotlib to draw the graph with seaborn
            fig, ax = plt.subplots()
            # Hisogram with density line to see the distribution
            sns.histplot(df[columna], kde=True, color='skyblue', ax=ax)
            ax.set_title(f'Distribucion de {columna}')

            # We show the graph in the app
            st.pyplot(fig)

        else:
            # If the column is not numeric then we show the most frecuent values
            st.write('Valores mas frecuentes:')
            st.write(df[columna].value_counts().head(5))

            # we create a bar graph with the 5 most common values
            fig, ax = plt.subplots()
            sns.countplot(y=df[columna], order=df[columna].value_counts(
            ).index[:5], palette='viridis', ax=ax)
            ax.set_title(f'Top 5 valores en {columna}')
            st.pyplot(fig)

        # We create a function that will create a PDF with the analysis we did on the column the user chose
        def generar_reporte(df, columna, nombre_archivo='reporte.pdf'):
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font('Arial', size=12)

            # We write the title and start showing the basic values we analysed such as rows and columns
            pdf.cell(200, 10, txt='Reporte de Analisis CSV', ln=True, align='C')
            pdf.ln(10)

            pdf.cell(200, 10, txt=f'Total de Filas : {df.shape[0]}', ln=True)
            pdf.cell(
                200, 10, txt=f'Total de Columnas : {df.shape[1]}', ln=True)
            pdf.cell(200, 10, txt=f'Columna analizada : {columna}', ln=True)
            pdf.ln(10)

            # Then again we verify if the column we analysed is numeric or not, then we show the data based on that
            if pd.api.types.is_numeric_dtype(df[columna]):
                pdf.cell(
                    200, 10, txt=f"Promedio: {df[columna].mean():.2f}", ln=True)
                pdf.cell(200, 10, txt=f"Máximo: {df[columna].max()}", ln=True)
                pdf.cell(200, 10, txt=f"Mínimo: {df[columna].min()}", ln=True)

                # After analysing the column we then make a graph with matplotlib and seaborn again
                fig, ax = plt.subplots()
                sns.histplot(df[columna], kde=True, color='skyblue', ax=ax)
                # We save the graph as an image
                plt.savefig('grafico.png')
                plt.close()

                # We print the graph in the pdf so that it is more complete
                pdf.image('grafico.png', x=10, y=None, w=180)

            else:
                pdf.cell(200, 10, txt="Valores más frecuentes:", ln=True)
                top = df[columna].value_counts().head(5)
                for valor, cuenta in top.items():
                    pdf.cell(200, 10, txt=f"{valor}: {cuenta}", ln=True)

                fig, ax = plt.subplots()
                sns.countplot(y=df[columna], order=df[columna].value_counts(
                ).index[:5], palette='viridis', ax=ax)
                ax.set_title(f'Top 5 valores en {columna}')
                plt.savefig('grafico.png')
                plt.close()

                pdf.image('grafico.png', x=10, y=None, w=180)

            pdf.output(nombre_archivo)
            print(f'Reporte generado: {nombre_archivo}')

        # We add a button on the web to let the user save the data as PDF
        if st.button('Generar Reporte en PDF'):
            generar_reporte(df, columna, 'reporte.pdf')
            with open('reporte.pdf', 'rb') as f:
                st.download_button('Descargar reporte PDF',
                                   f, file_name='reporte.pdf')
