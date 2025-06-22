# import os
# from fontTools.ttLib import TTFont

# # Define Punjabi (Gurmukhi) Unicode range
# PUNJABI_UNICODE_RANGE = range(0x0A00, 0x0A7F + 1)

# def is_unicode_punjabi_font(font_path):
#     try:
#         font = TTFont(font_path)
#         cmap = font['cmap'].getcmap(3, 10) or font['cmap'].getcmap(3, 1)
#         if cmap:
#             characters = set(cmap.cmap.keys())
#             if any(char in PUNJABI_UNICODE_RANGE for char in characters):
#                 return True
#     except Exception as e:
#         print(f"Error reading {font_path}: {e}")
#     return False

# def check_fonts_in_folder(folder_path):
#     font_files = [f for f in os.listdir(folder_path) if f.endswith(('.ttf', '.otf', '.TTF', '.OTF'))]
#     print(f"Total Fonts Found: {len(font_files)}\n")
    
#     for font_file in font_files:
#         font_path = os.path.join(folder_path, font_file)
#         result = is_unicode_punjabi_font(font_path)
#         print(f"{font_file}: {'✅ Unicode Punjabi' if result else '❌ Not Unicode Punjabi'}")

# # Change this to your font folder path
# folder_path = r"/home/scai/mtech/aib232080/scratch/trdg_2/trdg/fonts/pb"
# check_fonts_in_folder(folder_path)



# import os
# import shutil
# from fontTools.ttLib import TTFont

# # Define Punjabi (Gurmukhi) Unicode range
# PUNJABI_UNICODE_RANGE = range(0x0A00, 0x0A7F + 1)

# def is_unicode_punjabi_font(font_path):
#     """Check if the given font file contains Punjabi Unicode characters."""
#     try:
#         font = TTFont(font_path)
#         cmap = font['cmap'].getcmap(3, 10) or font['cmap'].getcmap(3, 1)
#         if cmap:
#             characters = set(cmap.cmap.keys())
#             return any(char in PUNJABI_UNICODE_RANGE for char in characters)
#     except Exception as e:
#         print(f"⚠️ Error reading {font_path}: {e}")
#     return False

# def delete_non_unicode_fonts(folder_path):
#     """Deletes fonts that do not support Punjabi Unicode."""
#     font_files = [f for f in os.listdir(folder_path) if f.endswith(('.ttf', '.otf', '.TTF', '.OTF'))]
    
#     if not font_files:
#         print("🛑 No font files found in the folder.")
#         return

#     for font_file in font_files:
#         font_path = os.path.join(folder_path, font_file)
#         if not is_unicode_punjabi_font(font_path):
#             print(f"❌ Deleting Non-Unicode Font: {font_file}")
#             os.remove(font_path)  # Deletes the font file
#         else:
#             print(f"✅ Keeping Unicode Punjabi Font: {font_file}")

# # Change this to your font folder path
# folder_path = r"/home/scai/mtech/aib232080/scratch/trdg_2/trdg/fonts/pb"
# delete_non_unicode_fonts(folder_path)


# import os
# from fontTools.ttLib import TTFont

# # Define Telugu Unicode range
# TELUGU_UNICODE_RANGE = range(0x0C00, 0x0C7F + 1)

# def is_unicode_telugu_font(font_path):
#     try:
#         font = TTFont(font_path)
#         cmap = font['cmap'].getcmap(3, 10) or font['cmap'].getcmap(3, 1)
#         if cmap:
#             characters = set(cmap.cmap.keys())
#             if any(char in TELUGU_UNICODE_RANGE for char in characters):
#                 return True
#     except Exception as e:
#         print(f"Error reading {font_path}: {e}")
#     return False

# def check_fonts_in_folder(folder_path):
#     font_files = [f for f in os.listdir(folder_path) if f.endswith(('.ttf', '.otf', '.TTF', '.OTF'))]
#     print(f"Total Fonts Found: {len(font_files)}\n")
    
#     for font_file in font_files:
#         font_path = os.path.join(folder_path, font_file)
#         result = is_unicode_telugu_font(font_path)
#         print(f"{font_file}: {'✅ Unicode Telugu' if result else '❌ Not Unicode Telugu'}")

# # Change this to your font folder path
# # folder_path = r"/home/scai/mtech/aib232080/scratch/trdg_2/trdg/fonts/te"
# # folder_path = r"/home/scai/mtech/aib232080/scratch/Anshul_ocr/fonts/telugu_fonts"
# folder_path = r"/home/scai/mtech/aib232080/scratch/synthtiger_2/resources/font/hi"
# check_fonts_in_folder(folder_path)


# import os
# from fontTools.ttLib import TTFont

# # Define Devanagari (Hindi) Unicode range
# DEVANAGARI_UNICODE_RANGE = range(0x0900, 0x097F + 1)

# def is_unicode_hindi_font(font_path):
#     try:
#         font = TTFont(font_path)
#         cmap = font['cmap'].getcmap(3, 10) or font['cmap'].getcmap(3, 1)
#         if cmap:
#             characters = set(cmap.cmap.keys())
#             if any(char in DEVANAGARI_UNICODE_RANGE for char in characters):
#                 return True
#     except Exception as e:
#         print(f"Error reading {font_path}: {e}")
#     return False

# def check_fonts_in_folder(folder_path):
#     font_files = [f for f in os.listdir(folder_path) if f.endswith(('.ttf', '.otf', '.TTF', '.OTF'))]
#     print(f"Total Fonts Found: {len(font_files)}\n")
    
#     for font_file in font_files:
#         font_path = os.path.join(folder_path, font_file)
#         result = is_unicode_hindi_font(font_path)
#         print(f"{font_file}: {'✅ Unicode Hindi' if result else '❌ Not Unicode Hindi'}")

# # Change this to your Hindi font folder path
# folder_path = r"/home/scai/mtech/aib232080/scratch/synthtiger_2/resources/font/hi"
# check_fonts_in_folder(folder_path)


# import os
# from fontTools.ttLib import TTFont

# # Define Oriya (Odia) Unicode range
# ORIYA_UNICODE_RANGE = range(0x0B00, 0x0B7F + 1)

# def is_unicode_oriya_font(font_path):
#     try:
#         font = TTFont(font_path)
#         cmap = font['cmap'].getcmap(3, 10) or font['cmap'].getcmap(3, 1)
#         if cmap:
#             characters = set(cmap.cmap.keys())
#             if any(char in ORIYA_UNICODE_RANGE for char in characters):
#                 return True
#     except Exception as e:
#         print(f"Error reading {font_path}: {e}")
#     return False

# def check_fonts_in_folder(folder_path):
#     font_files = [f for f in os.listdir(folder_path) if f.endswith(('.ttf', '.otf', '.TTF', '.OTF'))]
#     print(f"Total Fonts Found: {len(font_files)}\n")
    
#     for font_file in font_files:
#         font_path = os.path.join(folder_path, font_file)
#         result = is_unicode_oriya_font(font_path)
#         print(f"{font_file}: {'✅ Unicode Oriya' if result else '❌ Not Unicode Oriya'}")

# # Change this to your Oriya font folder path
# folder_path = r"/home/scai/mtech/aib232080/scratch/trdg_2/trdg/fonts/oriya_fonts"
# check_fonts_in_folder(folder_path)


import os
from fontTools.ttLib import TTFont

# Define Gujarati Unicode range
GUJARATI_UNICODE_RANGE = range(0x0A80, 0x0AFF + 1)

def is_unicode_gujarati_font(font_path):
    try:
        font = TTFont(font_path)
        cmap = font['cmap'].getcmap(3, 10) or font['cmap'].getcmap(3, 1)
        if cmap:
            characters = set(cmap.cmap.keys())
            if any(char in GUJARATI_UNICODE_RANGE for char in characters):
                return True
    except Exception as e:
        print(f"Error reading {font_path}: {e}")
    return False

def check_fonts_in_folder(folder_path):
    font_files = [f for f in os.listdir(folder_path) if f.endswith(('.ttf', '.otf', '.TTF', '.OTF'))]
    print(f"Total Fonts Found: {len(font_files)}\n")
    
    for font_file in font_files:
        font_path = os.path.join(folder_path, font_file)
        result = is_unicode_gujarati_font(font_path)
        print(f"{font_file}: {'✅ Unicode Gujarati' if result else '❌ Not Unicode Gujarati'}")

# Change this to your Gujarati font folder path
folder_path = r"/home/scai/mtech/aib232080/scratch/trdg_2/trdg/fonts/guj_fonts"
check_fonts_in_folder(folder_path)
