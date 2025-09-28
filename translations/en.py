#!/usr/bin/python
# -*-coding:Utf-8 -*
#

# Copyright 2013-2018 mirandir

# This file is part of Magic Collection.
#
# Magic Collection is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License (version 3) as published by
# the Free Software Foundation.
#
# Magic Collection is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Magic Collection.  If not, see <http://www.gnu.org/licenses/>.

# English strings for Magic Collection


def translate():
    translate = {}
    #########################
    translate["app_name"] = "Magic Collection"
    translate["language_name"] = "English"  # the current language name for this file
    # Gmenu
    translate["preferences"] = "Preferences"
    translate["preferences_of_mc"] = "Preferences of " + translate["app_name"]
    translate["importexport"] = "Restore / Backup"
    translate["import"] = "Restore a backup"
    translate["export"] = "Backup your data"
    translate["export_text"] = (
        "Export the collection as text file"  # Cannot be imported back
    )
    translate["help"] = "Help"
    translate["doc"] = "Documentation"
    translate["website"] = "Website"
    translate["tips"] = "Tips"
    translate["shortcuts"] = "Keyboard Shortcuts"
    translate["about"] = "About"
    translate["quit"] = "Quit"
    # About Window
    translate["about_comment"] = (
        "Informations, texts and pictures displayed about\nMagic: The Gathering are copyrighted by Wizards of the Coast."
    )

    translate["about_copyright"] = (
        translate["app_name"]
        + """ is not produced, affiliated or supported\nby Wizards of the Coast or Hasbro.

"""
        + translate["app_name"]
        + """ uses mtgjson.com for his database.
Many thanks to Sembiance and lsmoura for this website!
Price data are supplied by TCGplayer.com for information purpose only."""
    )

    translate["about_licence"] = (
        translate["app_name"]
        + """ is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License version 3 as published by the Free Software Foundation.

"""
        + translate["app_name"]
        + """ is distributed in the hope that it will be useful but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License version 3 for more details.

You should have received a copy of the GNU General Public License version 3 along with """
        + translate["app_name"]
        + """; if not, visit <http://www.gnu.org/licenses/>.

Logo of """
        + translate["app_name"]
        + """ by mirandir, under CC BY-NC-ND 3.0 : <https://creativecommons.org/licenses/by-nc-nd/3.0/deed/>

Images of color indicators by BaconCatBug (see <http://www.mtgsalvation.com/forums/creativity/artwork/494438-baconcatbugs-set-and-mana-symbol-megapack/>)
Math icons by Freepik (<http://www.flaticon.com/packs/mathbert-mathematics>)"""
    )
    translate["about_contributors"] = "Contributors &amp; testers"
    translate["about_contributors_list"] = (
        "Purphoros&&&Lilian&&&Giz&&&Delphine&&&mnskill&&&Alice&&&Stuffist"
    )

    # mainwindow
    translate["loading"] = "Loading..."
    translate["collection"] = "Collection"
    translate["decks"] = "Decks"
    translate["advancedsearch"] = "Advanced search"
    translate["search_card"] = "Search a card by name"
    translate["search_card_tooltip"] = "Search a card by name"
    translate["no_result"] = "No result."
    translate["aboutdialog_db"] = "DB"
    translate["choose_card"] = "Select"
    translate["results"] = "%%% results:"
    translate["coll_busy"] = (
        "An operation is pending on the collection, impossible to quit for now."
    )
    # non english helpers for simple search - without accents or uppercase letters (must be empty for the english translation file)
    translate["forest"] = ""
    translate["island"] = ""
    translate["mountain"] = ""
    translate["swamp"] = ""
    translate["plains"] = ""
    # Database
    translate["db_damaged"] = (
        "The database seems broken. Restart "
        + translate["app_name"]
        + " to solve the problem."
    )
    translate["no_internet_update_db"] = (
        "Unable to check updates of the database: no internet connection found."
    )
    translate["no_internet_download_db"] = (
        "Unable to download the update of the database: no internet connection found."
    )
    translate["error_download_db"] = "Error when downloading the cards database."
    translate["problem_db"] = (
        "Impossible to download/load the cards database.\n"
        + translate["app_name"]
        + " cannot be use without its database."
    )
    translate["warning_ver_db"] = (
        "This version of the database will not work with your version of "
        + translate["app_name"]
        + ". Please update "
        + translate["app_name"]
        + "."
    )
    translate["changelog_db"] = "Changelog:"
    translate["new_update_db"] = (
        "An update of the cards database is available.%%%\nWould you like to download it now?"
    )
    translate["downloading_db"] = "Downloading of the database..."
    translate["downloading_symbols"] = "Downloading of the symbols..."
    translate["checking_db_update"] = "Checking of update of the database..."
    # advanced search
    translate["searching"] = "Searching..."
    translate["please_wait"] = "May take some time..."
    translate["search_ad"] = "Search"
    translate["operator_choice"] = "Logical operator"
    translate["operator_and"] = "and"
    translate["operator_or"] = "or"
    translate["card"] = "card"
    translate["cards"] = "cards"
    translate["card_result"] = "result"
    translate["cards_result"] = "results"
    translate["list_editions"] = "Editions"
    translate["add_edition"] = "Add edition"
    translate["name_ad"] = "Name"
    translate["edition_ad"] = "Edition"
    translate["colors_ad"] = "Color(s)"
    translate["manacost_eg_ad"] = "Mana Cost"
    translate["cmc_ad"] = "Converted Cost"
    translate["type_ad"] = "Type"
    translate["artist_ad"] = "Artist"
    translate["text_ad"] = "Text"
    translate["flavor_ad"] = "Flavor"
    translate["power_ad"] = "Power"
    translate["toughness_ad"] = "Toughness"
    translate["loyalty_ad"] = "Loyalty"
    translate["entry_eq_ad"] = "Equal"
    translate["entry_inf_eq_ad"] = "Equal or less"
    translate["entry_sup_eq_ad"] = "Equal or greater"
    translate["entry_diff"] = "Different"
    translate["nb_cards_in_db"] = "There are almost %%% cards in the database."
    translate["column_internal_id"] = "internal id"
    translate["column_english_name"] = "Name"  # must be 'Name' for the english file
    translate["column_english_name_complete"] = (
        "Name"  # must be 'Name' for the english file
    )
    translate["column_edition"] = "Edition"
    translate["column_edition_complete"] = "Edition"
    translate["column_nonenglish_name"] = "Non-english Name"
    translate["column_name_name_french"] = "French Name"
    translate["column_name_name_chinesetrad"] = "Chinese Name (trad)"
    translate["column_name_name_chinesesimp"] = "Chinese Name (simpl)"
    translate["column_name_name_german"] = "German Name"
    translate["column_name_name_italian"] = "Italian Name"
    translate["column_name_name_japanese"] = "Japanese Name"
    translate["column_name_name_korean"] = "Korean Name"
    translate["column_name_name_portuguesebrazil"] = "Portuguese Name (B)"
    translate["column_name_name_portuguese"] = "Portuguese Name"
    translate["column_name_name_russian"] = "Russian Name"
    translate["column_name_name_spanish"] = "Spanish Name"
    translate["column_colors"] = "Color"
    translate["column_colors_complete"] = "Color(s)"
    translate["column_cmc"] = "CMC"
    translate["column_cmc_complete"] = "Converted Mana Cost"
    translate["column_type"] = "Type"
    translate["column_type_complete"] = "Type"
    translate["column_artist"] = "Artist"
    translate["column_artist_complete"] = "Artist"
    translate["column_power"] = "Power"
    translate["column_toughness"] = "Toughness"
    translate["column_rarity"] = "Rarity"
    translate["column_rarity_complete"] = "Rarity"
    translate["column_nb"] = "#"
    translate["column_nb_complete"] = "Quantity"
    translate["column_coll_ed_nb_complete"] = "Collection number"
    translate["column_coll_ed_nb"] = "N°"
    translate["column_prices"] = "Price"
    translate["cmc_only_number"] = (
        "Searching by Converted Mana Cost can only be done with integers."
    )
    translate["power_only_number"] = (
        "Searching by Power can only be done with integers."
    )
    translate["toughness_only_number"] = (
        "Searching by Toughness can only be done with integers."
    )
    translate["loyalty_only_number"] = (
        "Searching by Loyalty can only be done with integers."
    )
    # rarity
    translate["rarity"] = "Rarity"
    translate["mythic"] = "Mythic"
    translate["rare"] = "Rare"
    translate["uncommon"] = "Uncommon"
    translate["common"] = "Common"
    translate["basic_land"] = "Basic land"
    translate["special"] = "Special"
    # non english helpers - without accents or uppercase letters (must be empty for the english translation file)
    translate["artifact"] = ""
    translate["artifacts"] = ""
    translate["enchantment"] = ""
    translate["enchantments"] = ""
    translate["instant"] = ""
    translate["instants"] = ""
    translate["land"] = ""
    translate["lands"] = ""
    translate["planeswalker"] = ""
    translate["planeswalkers"] = ""
    translate["creature"] = ""
    translate["creatures"] = ""
    translate["sorcery"] = ""
    translate["sorceries"] = ""
    translate["token"] = ""
    translate["tokens"] = ""
    translate["emblem"] = ""
    translate["emblems"] = ""
    translate["counter"] = ""
    translate["counters"] = ""
    translate["red"] = ""
    translate["green"] = ""
    translate["black"] = ""
    translate["blue"] = ""
    translate["white"] = ""
    translate["colorless"] = ""
    translate["h_mythic"] = ""
    translate["h_rare"] = ""
    translate["h_uncommon"] = ""
    translate["h_common"] = ""
    translate["h_basic_land"] = ""
    translate["h_special"] = ""
    # card viewer
    translate["open_gatherer"] = "Open the Gatherer"
    translate["open_display_price"] = (
        "Informative price: %%%;;;"  # ';;;' is replaced by the price, '%%%' by the currency
    )
    translate["other_edition"] = "Other print"
    translate["other_editions"] = "Other prints"
    translate["download_card_no_internet"] = (
        "Unable to download the picture of the card: no internet connection found."
    )
    translate["add_card_question"] = "Add %%% to the collection?"
    translate["add_card_question_without_collection"] = "Add %%%?"
    translate["add_cards_question"] = "Add the %%% following cards to the collection?"
    translate["add_cards_question_without_collection"] = "Add the %%% following cards?"
    translate["warning_nb_card"] = "(Warning: this operation will take some time)"
    translate["quantity"] = "Quantity:"
    translate["details"] = "Details"
    translate["add_button_validate"] = "Add"
    translate["add_button_wait"] = "Operation pending..."
    translate["add_condition"] = "Condition"
    translate["condition_mint"] = "Mint"
    translate["condition_near_mint"] = "Near Mint"
    translate["condition_excellent"] = "Excellent"
    translate["condition_played"] = "Played"
    translate["condition_poor"] = "Poor"
    translate["add_lang"] = "Language"
    translate["add_foil"] = "Foil"
    translate["add_loaned"] = "Loaned to"
    translate["add_comment"] = "Comment"
    translate["morebutton_tooltip"] = "More information"
    translate["dfbutton_seeotherside_tooltip"] = "See the other side"
    translate["dfbutton_returncard_tooltip"] = "Reverse the card"
    translate["dfbutton_meldsto_tooltip"] = "Melds to..."
    translate["dfbutton_meldedfrom_tooltip"] = "Melded from..."
    translate["cv_add_collection"] = "To the collection"
    translate["cv_add_proxies"] = "As a proxy"
    translate["cv_add_proxies_s"] = "As proxies"
    # collection
    translate["db_coll_error"] = "Unable to read the collection."
    translate["coll_empty_welcome"] = (
        "Welcome to "
        + translate["app_name"]
        + "!\n\Your collection is empty. You can search cards with the top left icon, or with the advanced search.\nWhen you find a card to add, move your mouse over his picture and click the '+'."
    )
    translate["nb_card_coll_s"] = "%%% cards in the collection"
    translate["nb_card_coll"] = "%%% card in the collection"
    translate["info_select_none_coll"] = "(no selection)"
    translate["info_select_coll"] = "(1 selection)"
    translate["info_selects_coll"] = "(%%% selections)"
    translate["coll_updated"] = (
        "The collection has changed since this search. The results may be obsolete"
    )
    translate["searching_coll"] = "Search in the collection"
    translate["condition_coll"] = "Condition"
    translate["lang_coll"] = "Language"
    translate["foil_coll"] = "Foil"
    translate["loaned_coll"] = "Loaned to"
    translate["comment_coll"] = "Comment"
    translate["date_coll"] = "Date Added"
    translate["quantity_card_coll"] = "Quantity"
    translate["in_deck"] = "In the deck"
    translate["search_coll"] = "Search"
    translate["back_to_coll"] = "Back to the collection"
    translate["coll_button_search_wait"] = "Operation pending..."
    translate["nb_card_found_coll_s"] = "%%% results"
    translate["nb_card_found_coll"] = "%%% result"
    translate["foil_yes"] = "yes"
    translate["foil_no"] = "no"
    translate["foil_only_yesno"] = (
        "Searching by Foil can only be done with: 1, 0, "
        + translate["foil_yes"]
        + ", "
        + translate["foil_no"]
        + "."
    )
    translate["placeholder_date"] = "YYYY-MM-DD"  # y-m-d
    translate["date_format"] = (
        "Searching by Date added to the collection can only be done with the YYYY-MM-DD format (Year-Month-Day)."
    )
    translate["quantity_card_coll_only_number"] = (
        "Searching by Quantity can only be done with integers."
    )
    translate["change_quantity"] = "Change quantity"
    translate["change_quantity_validate"] = "Ok"
    translate["add_to_deck_all"] = "All the selection"
    translate["delete_select"] = "Delete the selection"
    translate["delete_select_warning"] = (
        "All copies of these cards will be DELETED.\nAre you sure?"
    )
    translate["delete_all"] = "Delete the collection and the decks"
    translate["delete_all_warning"] = (
        "All your decks and all cards in your collection will be DELETED.\nAre you sure?"
    )
    translate["estimate_select"] = "Estimate the selection"
    translate["estimate_all"] = "Estimate the collection"
    translate["state_card_coll_date"] = (
        "This card has been added to the collection on <b>{y}/{m}/{d}</b>."
    )
    translate["state_card_coll_deck"] = "It's used in the deck <b>{deck}</b>."
    translate["state_card_coll_deck_side"] = (
        "It's used in the sideboard of the deck <b>{deck}</b>."
    )
    translate["search_collection_button"] = "Search in the collection"
    translate["search_collection_tooltip"] = "Search in the cards of the collection"
    translate["show_details_tooltip"] = "Show details"
    translate["change_quantity_tooltip"] = "Change quantity"
    translate["add_deck_tooltip"] = "Add to a deck"
    translate["estimate_cards_tooltip"] = "Estimate cards"
    translate["delete_cards_tooltip"] = "Delete cards"
    translate["copy_details_tooltip"] = (
        "Copy the details of this card over each other card displayed"
    )
    translate["delete_cards_details_tooltip"] = "Delete the collection"
    # decks
    translate["list_decks_nb"] = "Decks (%%%)"
    translate["create_new_deck"] = "Create a new deck"
    translate["estimate_deck"] = "Estimate the deck"
    translate["delete_deck"] = "Delete the deck"
    translate["decks_empty_welcome"] = (
        "You have not yet added a deck in "
        + translate["app_name"]
        + ".\nClick here to add one."
    )
    translate["create_new_deck_name"] = "Name of the deck to add"
    translate["create_new_deck_ok"] = "Ok"
    translate["comment_deck"] = "Comment of the deck"
    translate["edit_name_deck"] = "Name of the deck"
    translate["edit_comment_name_deck"] = "Edit the informations of the deck"
    translate["change_deck_name"] = "Change"
    translate["decks_click_deck"] = "Click on a deck to show his cards."
    translate["nb_cards_in_deck"] = "%%% card"
    translate["nb_cards_in_deck_s"] = "%%% cards"
    translate["decks_sideboard"] = "Sideboard: "
    translate["decks_in_sideboard"] = "(%%% in the sideboard)"
    translate["decks_order_cards_sideboard"] = "{cards} {sideboard}"
    translate["decks_add_to_sideboard"] = "Add to the sideboard"
    translate["move_to_other_deck"] = "Move the selection to another deck"
    translate["delete_deck_warning"] = "Are you sure you want to remove the deck %%%?"
    translate["delete_from_deck_tooltip"] = "Delete from the deck"
    translate["move_to_other_deck_tooltip"] = "Move to another deck"
    translate["sideboard_tooltip"] = "Sideboard"
    translate["sideboard_add"] = "Put in the sideboard"
    translate["sideboard_remove"] = "Remove from the sideboard"
    # languages
    translate["l_english"] = "English"
    translate["l_chinese"] = "Chinese"
    translate["l_french"] = "French"
    translate["l_german"] = "German"
    translate["l_italian"] = "Italian"
    translate["l_japanese"] = "Japanese"
    translate["l_korean"] = "Korean"
    translate["l_portuguese"] = "Portuguese"
    translate["l_russian"] = "Russian"
    translate["l_spanish"] = "Spanish"
    # prices
    translate["error_download_db_prices"] = (
        "Error when downloading the cards prices database."
    )
    translate["no_internet_download_db_prices"] = (
        "Unable to download the update of the cards prices database: no internet connection found."
    )
    translate["prices_db_damaged"] = (
        "The cards prices database seems broken. You can download it again to fix the problem."
    )
    translate["estimate_dialog_title"] = "Estimate"
    translate["estimate_dialog_select"] = "The selection is estimated at %%%."
    translate["estimate_dialog_collection"] = "The collection is estimated at %%%."
    translate["estimate_dialog_deck"] = "The deck ;;; is estimated at %%%."
    translate["estimate_ok"] = "Ok"
    translate["estimate_x_cards_without_price"] = "1 card without estimation"
    translate["estimate_x_cards_without_price_s"] = "%%% cards without estimation"
    # configuration
    translate["config_display"] = "Display"
    translate["config_editions"] = "Editions"
    translate["config_ext_fr_name"] = (
        "Display the French name for editions when it exists"
    )
    translate["config_ext_sort_as"] = "In the advanced search, sort editions by:"
    translate["config_ext_sort_as_date"] = "Release date"
    translate["config_ext_sort_as_name"] = "Name"
    translate["config_searches"] = "Searches"
    translate["config_no_reprints"] = "Don't show the different prints of the same card"
    translate["config_cardviewer"] = "Cardviewer"
    translate["config_show_en_name_in_card_viewer"] = (
        "Show the english name in the cardviewer"
    )
    translate["config_collection"] = "Add to the collection"
    translate["config_add_collection_show_details"] = (
        "Show details when adding cards to the collection"
    )
    translate["config_general_aspect"] = "General aspect"
    translate["config_dark_theme"] = "Use the dark-variant of the theme"
    translate["config_columns"] = "Columns"
    translate["config_columns_helper"] = (
        "You can change the order by dragging and dropping the column headings."
    )
    translate["config_column_enabled"] = "Enabled"
    translate["config_nonenglish_names"] = "Non-english Names"
    translate["config_fr_language"] = "Language for the Non-english Name column:"
    translate["config_columns_order_disp"] = "Display and order of the columns"
    translate["config_columns_collection"] = "Columns - Collection"
    translate["config_columns_decks"] = "Columns - Decks"
    translate["config_columns_as"] = "Columns - Advanced search"
    translate["config_internet"] = "Web"
    translate["config_defaultvalues"] = "Default values"
    translate["config_defaultvalues_addcoll_details"] = (
        "Add to the collection - Details"
    )
    translate["config_defaultvalues_condition"] = "Default value for Condition:"
    translate["config_defaultvalues_lang"] = "Default value for Language:"
    translate["config_pics_cards"] = "Cards pictures"
    translate["config_download_pic_collection_decks"] = (
        "Download the pictures in the Collection et the Decks"
    )
    translate["config_download_pic_as"] = "Download the pictures in the Advanced search"
    translate["config_connection"] = "Connection"
    translate["config_not_internet_popup"] = (
        "Display a warning when no internet connection is found"
    )
    translate["config_cardsprices"] = "Cards prices"
    translate["config_cardsprices_download_first"] = (
        "First click here to download cards prices."
    )
    translate["config_cardsprices_download"] = "Download cards prices"
    translate["config_prices_show"] = "Show the prices"
    translate["config_cardsprices_show"] = (
        "Show the prices of the cards in the 'More information' menu"
    )
    translate["config_price_cur"] = "Currency:"
    translate["config_price_dollars"] = "Dollars"
    translate["config_price_euros"] = "Euros"
    translate["config_prices_update"] = "Prices update"
    translate["config_prices_autoupdate"] = (
        "Automatically update the prices when launching " + translate["app_name"]
    )
    translate["config_prices_version"] = "Prices database version: <b>%%%</b>."
    translate["config_cardsprices_update"] = "Update the prices"
    translate["config_cardsprices_checking_update"] = (
        "Checking updates for the cards prices..."
    )
    translate["config_cardsprices_downloading"] = "Downloading of the cards prices..."
    translate["config_need_restart"] = "Need a restart of " + translate["app_name"]
    translate["config_pic_cards"] = "Cards pictures"
    translate["config_pic_cards_downloaded"] = "Downloaded pictures"
    translate["config_pic_cards_downloaded_editions_intro_none"] = (
        "No picture downloaded yet."
    )
    translate["config_pic_cards_downloaded_editions_intro"] = (
        "Pictures had been downloaded for editions:"
    )
    translate["config_pic_cards_delete"] = "Delete the pictures of the selected edition"
    translate["config_pic_cards_delete_all"] = "Delete all downloaded pictures"
    translate["config_pic_cards_size_all"] = "Size of the pictures: "
    translate["config_pic_cards_size_b"] = "b"
    translate["config_pic_cards_size_ko"] = "ko"
    translate["config_pic_cards_size_mo"] = "Mo"
    translate["config_pic_cards_size_go"] = "Go"
    translate["config_pic_cards_size_to"] = "To"
    translate["config_pic_cards_size_unit"] = "{VALUE} {SIZE}"
    # export
    translate["exportimport_filetype"] = "Files of " + translate["app_name"]
    translate["text_filetype"] = "Text files"
    translate["export_collection_busy"] = (
        "Unable to backup your data, the collection is busy."
    )
    translate["export_filename"] = "Magic collection of %user% (%date%)"
    translate["export_write_impossible"] = (
        "Unable to save th file.\nYou may not have the required permissions. Make sure the location is correct and try again."
    )
    # import
    translate["import_collection_busy"] = (
        "Unable to restore your data, the collection is busy."
    )
    translate["import_areyousure"] = (
        "Your collection and your decks will be replaced.\nAre you sure?"
    )
    translate["import_error"] = "Error when importing file."
    translate["import_success"] = "Restore was successful."
    translate["import_oldformat"] = (
        "Converting your collection and your decks. Can take some time..."
    )
    translate["import_oldformat_error_sqlite_is_here"] = (
        "Error: "
        + translate["app_name"]
        + " is unable to convert your collection and your decks to the new format, because a collection already exists in this format. This should not happen unless you have manually copied the old files in the folder where "
        + translate["app_name"]
        + " stores your data. If it's not the case, thank you to report the problem."
    )
    translate["import_oldformat_error_collection0810"] = (
        "Error when converting the collection. "
        + translate["app_name"]
        + " can only convert the collection used with "
        + translate["app_name"]
        + " 0.8.10."
    )
    translate["import_useindeck"] = "used in the deck"
    translate["import_conver"] = "Convert data"
    translate["import_oldformat_finish"] = (
        translate["app_name"]
        + " finished converting your data, but some cards were not found. This can happen with some tokens that previously had color in their name. You should copy this list in a safe place, in order to add these cards again in "
        + translate["app_name"]
        + "."
    )
    translate["import_oldformat_finish_ok"] = "Converting your data is complete."
    # tips
    translate["tips_general"] = "General"
    translate[
        "tips_general_text"
    ] = """● You can select more than one card with regular shortcuts (Ctrl + mouse left, Shift + mouse left, Shift + arrows). Then you can perform operations on many cards at the same time.
        
● In the Collection, bolded lines have at least one card with a comment, and italicized lines have at least one card used in a deck.

● In Decks, italicized lines are proxies or cards in the sideboard.

● In the Advanced Search, bolded lines are cards in your collection."""
    translate["tips_search"] = "Search"
    translate["tips_search_text_partname"] = (
        """● Type the complete name of a card is not mandatory to find it."""
    )
    translate["tips_search_text_nonenglishname"] = (
        """● The database has the names of the cards for each language printed. You can type non-english names in a search."""
    )
    translate["tips_search_text_logicop"] = (
        """● All search fields (unless '"""
        + translate["quantity_card_coll"]
        + """') allow the use of some limited logical operators ':"""
        + translate["operator_and"]
        + """:' and ':"""
        + translate["operator_or"]
        + """:'."""
    )
    translate["tips_search_text_op"] = (
        """● In all search fields (unless '""" + translate["cmc_ad"] + "', '"
        "" + translate["column_power"] + "', '"
        ""
        + translate["column_toughness"]
        + """', '"""
        + translate["loyalty_ad"]
        + """' and '"""
        + translate["quantity_card_coll"]
        + """'), add one '!' before your search will look for the opposite."""
    )
    translate["tips_search_text_null"] = (
        """● The fields '"""
        + translate["text_ad"]
        + """', '"""
        + translate["flavor_ad"]
        + """', '"""
        + translate["condition_coll"]
        + """', '"""
        + translate["lang_coll"]
        + """', '"""
        + translate["loaned_coll"]
        + """', '"""
        + translate["comment_coll"]
        + """' and '"""
        + translate["in_deck"]
        + """' allow the use of '¤' (or 'ø') to indicate an empty value. For example, type 'goblin' in the field '"""
        + translate["type_ad"]
        + "' and '¤' in the field '"
        ""
        + translate["text_ad"]
        + """' will retrieve all goblins without text. This works with the empty value ('goblin' in the field '"""
        + translate["type_ad"]
        + """' and '!¤' in the field '"""
        + translate["text_ad"]
        + """' will retrieve all goblins with text)."""
    )
    translate["tips_search_text_spetext"] = (
        """● In the field '"""
        + translate["name_ad"]
        + """', you can type '//' to retrieve all the splited cards, '<>' for the inverted cards, '||' for the double-faced cards and '~~' for cards with Meld."""
    )
    translate["tips_search_text_rarity"] = (
        """● The field '"""
        + translate["column_rarity"]
        + """' allows the next values: '"""
        + translate["mythic"]
        + """', '"""
        + translate["rare"]
        + """', '"""
        + translate["uncommon"]
        + """', '"""
        + translate["common"]
        + """', '"""
        + translate["basic_land"]
        + """' and '"""
        + translate["special"]
        + """'."""
    )
    translate["tips_search_text_manacost"] = (
        """● Values typed in the field '"""
        + translate["manacost_eg_ad"]
        + """' must be surrounded by brackets ('{' and '}')."""
    )
    translate["tips_search_text_colors"] = (
        """● The field '"""
        + translate["colors_ad"]
        + """' allows the name and the first letter of the colors."""
    )
    translate["tips_search_text_condition"] = (
        """● The field '"""
        + translate["add_condition"]
        + """' allows the next values: '"""
        + translate["condition_mint"]
        + """', '"""
        + translate["condition_near_mint"]
        + """', '"""
        + translate["condition_excellent"]
        + """', '"""
        + translate["condition_played"]
        + """' and '"""
        + translate["condition_poor"]
        + """'."""
    )
    translate["tips_proxies"] = "Proxies"
    translate["tips_proxies_text"] = (
        """● You can add proxies to a deck. Display the chosen card in the Decks, then click the add button. Choose '"""
        + translate["cv_add_proxies"]
        + """'."""
    )
    translate["shortcuts_globals"] = "Globals"
    translate["shortcuts_simple_search"] = "Search by name"
    translate["shortcuts_switch_collection"] = "Switch to the Collection"
    translate["shortcuts_switch_decks"] = "Switch to the Decks"
    translate["shortcuts_switch_adsearch"] = "Switch to the Advanced search"
    #########################
    return translate
