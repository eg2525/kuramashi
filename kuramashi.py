import streamlit as st
import pandas as pd
from io import BytesIO

def main():
    st.title('Excel情報転記アプリ')

    # Excelファイルのアップロード部分
    st.subheader('二つのExcelファイルをアップロードしてください')
    file1 = st.file_uploader('一つ目のExcelファイルをアップロード', type=['xlsx'], key="file1")
    file2 = st.file_uploader('二つ目のExcelファイルをアップロード', type=['xlsx'], key="file2")

    if file1 and file2:
        sheets_file1 = pd.ExcelFile(file1).sheet_names
        sheets_file2 = pd.ExcelFile(file2).sheet_names

        st.subheader('各ファイルからシートを選択してください')
        selected_sheet1 = st.selectbox('一つ目のファイルからシートを選択', sheets_file1, key="selected_sheet1")
        selected_sheet2 = st.selectbox('二つ目のファイルからシートを選択', sheets_file2, key="selected_sheet2")

        df1 = pd.read_excel(file1, sheet_name=selected_sheet1, header=5)
        df2 = pd.read_excel(file2, sheet_name=selected_sheet2, header=0)

        st.subheader('2のシートのヘッダー名に対応する1のシートのヘッダーを選択してください')
        header_mappings = {}
        for col in df2.columns:
            options = ['転記しない'] + list(df1.columns)
            selected_option = st.selectbox(f'2のシートのヘッダー "{col}" に対応する1のシートのヘッダーを選択:', options, key=col+"_header")
            header_mappings[col] = selected_option

        if st.button('転記実行'):
            st.write('情報転記を実行中...')

            for col2, col1 in header_mappings.items():
                if col1 != '転記しない':
                    df2[col2] = df1[col1]

            # CSVとしてデータをエンコード
            csv_bytes = BytesIO()
            df2.to_csv(csv_bytes, index=False, encoding='cp932')
            csv_bytes.seek(0)

            st.download_button(label='完成したシートをダウンロード',
                               data=csv_bytes,
                               file_name='completed_sheet.csv',
                               mime='text/csv')

            st.write('情報転記が完了しました！')

if __name__ == "__main__":
    main()
