import os
from bs4 import BeautifulSoup
from utils import get_config


def player_identifier():
    """
    Callback for watch_for_export: processes the received HTML and displays
    players with a training score above the threshold, plus scroll offset
    to the first qualifying player.
    """
    config = get_config()
    print_dir = config.get("print_dir", "~/Documents/Sports Interactive/Football Manager 2023")
    print_file = config.get("print_file_name", "Untitled.html")

    print_file_path = os.path.expanduser(print_dir + "/" + print_file)

    try:
        with open(print_file_path, "r", encoding="utf-8") as f:
            html = f.read()
    except FileNotFoundError:
        print(f"Couldn't open the file: {print_file_path}")
        return

    soup = BeautifulSoup(html, "html.parser")

    # Buscar la tabla con columna "Trn Rat"
    target_table = None
    for table in soup.find_all("table"):
        headers = [th.get_text(strip=True) for th in table.find_all("th")]
        if "Trn Rat" in headers:
            target_table = table
            break

    if not target_table:
        print("Couldn't find the player ratings table")
        return

    # Obtener threshold desde config si no se pasó
    threshold = float(config.get("min_score_to_praise", "7.5"))

    players = []
    scroll_count = 0

    for row in target_table.find_all("tr")[1:]:  # saltamos header
        cols = row.find_all("td")
        if len(cols) < 4:
            continue

        name = cols[1].get_text(strip=True)
        try:
            rating = float(cols[3].get_text(strip=True))
        except ValueError:
            continue

        # Guardar jugadores con puntaje >= threshold
        if rating >= threshold:
            players.append({"name": name, "rating": rating})
            # Si el jugador es "- -", hay que scrollear
            if name == "- -":
                scroll_count += 1

    print(f"File processed: {print_file_path}")
    print(f"Scroll needed for hidden players with rating >= {threshold}: {scroll_count}")
    print(f"Number of scrolls required: {scroll_count}")
    print("Qualifying players:")
    for p in players:
        print(f"{p['name']} ({p['rating']})")
