import streamlit as st
import pandas as pd

def main():
    st.title('Excel情報転記アプリ')

    # Excelファイルのアップロード部分
    st.subheader('二つのExcelファイルをアップロードしてください')
    file1 = st.file_uploader('一つ目のExcelファイルをアップロード', type=['xlsx'], key="file1")
    file2 = st.file_uploader('二つ目のExcelファイルをアップロード', type=['xlsx'], key="file2")

    # 両方のファイルがアップロードされた場合の処理
    if file1 and file2:
        # アップロードされたファイルからシート名を取得
        sheets_file1 = pd.ExcelFile(file1).sheet_names
        sheets_file2 = pd.ExcelFile(file2).sheet_names

        # シートを選択するためのプルダウンメニュー
        st.subheader('各ファイルからシートを選択してください')
        selected_sheet1 = st.selectbox('一つ目のファイルからシートを選択', sheets_file1, key="selected_sheet1")
        selected_sheet2 = st.selectbox('二つ目のファイルからシートを選択', sheets_file2, key="selected_sheet2")

        # シート選択後の処理
        if st.button('シート選択完了'):
            # 選択されたシートをセッションステートに保存
            st.session_state["df1"] = pd.read_excel(file1, sheet_name=selected_sheet1, header=5)  # 6行目がヘッダー
            st.session_state["df2"] = pd.read_excel(file2, sheet_name=selected_sheet2, header=0)  # 1行目がヘッダー

    # ヘッダーのマッピング処理
    if "df1" in st.session_state and "df2" in st.session_state:
        st.subheader('2のシートのヘッダー名に対応する1のシートのヘッダーを選択してください')
        for col in st.session_state["df2"].columns:
            options = list(st.session_state["df1"].columns)
            st.session_state[col] = st.selectbox(f'2のシートのヘッダー "{col}" に対応する1のシートのヘッダーを選択:', options, key=col)

# アプリを実行
if __name__ == "__main__":
    main()
