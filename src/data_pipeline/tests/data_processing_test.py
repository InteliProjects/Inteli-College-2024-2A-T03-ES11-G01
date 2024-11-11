import unittest
import os
import pandas as pd
from datetime import datetime
import core.data_processing as data_processing

class TestConvertFunctions(unittest.TestCase):
    def setUp(self):
        self.temp_folder = "temp_test"
        os.makedirs(self.temp_folder, exist_ok=True)

        self.csv_file = "test_file.csv"
        self.df = pd.DataFrame({
            "col1": [1, 2, 3],
            "col2": ["a", "b", "c"]
        })
        self.df.to_csv(os.path.join(self.temp_folder, "test_file.csv"), index=False)

    def tearDown(self):
        if os.path.exists(self.temp_folder):
            for file in os.listdir(self.temp_folder):
                file_path = os.path.join(self.temp_folder, file)
                os.remove(file_path)
            os.rmdir(self.temp_folder)

    def test_convert_to_parquet(self):
        data_processing.convert_to_parquet(self.csv_file, self.temp_folder)

        parquet_file = os.path.join(self.temp_folder, "test_file.parquet")
        self.assertTrue(os.path.exists(parquet_file), f"Arquivo {parquet_file} não foi criado.")

        df_original = pd.read_csv(os.path.join(self.temp_folder, self.csv_file))
        df_parquet = pd.read_parquet(parquet_file)
        pd.testing.assert_frame_equal(df_original, df_parquet, check_like=True)

    def test_convert_to_other_type(self):
        data_processing.convert_to_other_type(self.csv_file, self.temp_folder)

        json_file = os.path.join(self.temp_folder, "test_file.json")
        self.assertTrue(os.path.exists(json_file), f"Arquivo {json_file} não foi criado.")

        df_original = pd.read_csv(os.path.join(self.temp_folder ,self.csv_file))
        df_json = pd.read_json(json_file)
        pd.testing.assert_frame_equal(df_original, df_json, check_like=True)

    def test_prepare_dataframe_for_insert(self):
        df_with_extra_columns = data_processing.prepare_dataframe_for_insert("test_file.parquet", self.df)
        
        self.assertIn('date_ingestion', df_with_extra_columns.columns)
        self.assertIn('data_row', df_with_extra_columns.columns)
        self.assertIn('tag', df_with_extra_columns.columns)

        # Verify tag
        self.assertEqual(df_with_extra_columns['tag'].iloc[0], "test_file")

        # Verify date_ingestion column
        self.assertIsInstance(df_with_extra_columns['date_ingestion'].iloc[0], datetime)

    def test_validate_file_valid(self):
        valid_df = pd.DataFrame({
            "cod_prod": [1, 2, 3],
            "data_inicio": ["2023-01-01", "2023-01-02", "2023-01-03"],
            "data_fim": ["2023-12-31", "2023-12-30", "2023-12-29"],
            "preco": [100.0, 150.0, 200.0]
        })

        is_valid = data_processing.validate_file("sku_price", valid_df)
        self.assertTrue(is_valid, "O arquivo CSV deveria ser válido, mas foi considerado inválido.")

    def test_validate_file_invalid(self):
        invalid_df = pd.DataFrame({
            "invalid_column": [1, 2, 3],
            "another_column": ["a", "b", "c"]
        })

        is_valid = data_processing.validate_file("sku_price", invalid_df)
        self.assertFalse(is_valid, "O arquivo CSV deveria ser inválido, mas foi considerado válido.")

if __name__ == "__main__":
    unittest.main()
