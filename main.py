import Helpers.data_manip as dm
import pandas as pd


def main():
    game_list = [] 
    pages = dm.number_of_pages()
    total_records = dm.get_full_game_list(pages)
    print(f"{len(total_records)} games in the file.")
    total_trimmed_records = dm.trim_data(total_records)    
    normalized_records = dm.normalize_prices(total_trimmed_records)
    add_margin = dm.add_margin(normalized_records)
    game_list = dm.transform_data_for_d_frame(add_margin)
    overall_dFrame = pd.DataFrame(game_list)
    overall_dFrame.to_excel("output.xlsx", index=False, engine='openpyxl')
    print("File has been created.")
    
if __name__ == "__main__":
    main()