# ------------------------------------------------------------------ # 
# PROG1: Projekt Clovece nehnevaj sa                                 #
#                                                                    #
# Akademicky rok: 2020/2021                                          #
#                                                                    # 
# Autor: Copyright (c) Jozef Szimeth                                 #
#                                                                    #
# Poznamka: Pri odovzdani su nastaveny dvaja hraci. Program dokaze   #
# odsimulovat aj styroch hracov, je mozne odskusat so zmenou hodnoty #
# premennej PLAYER_COUNT (riadok 19) na 4. Rozpis implementovanych   #
# pravidiel je na spodku suboru.                                     #
# ------------------------------------------------------------------ #


from random import randint, choice
from math import sin, cos, radians


PLAYER_COUNT = 2
ROAD_TILE = "*"
HOME_TILE = "O"
BOARD_CENTER_TILE = "X"
PLAYER_FIGURES = ("A", "B", "P", "Z")


def main():
  """Entrypoint of the program."""
  if PLAYER_COUNT > 4 or PLAYER_COUNT < 1:
    print("\n[Error]: Simulation cannot be started. PLAYER_COUNT " +
          "should be an integer between 1 and 4.")
    return
  n = get_user_input()
  game_board = gensachovnicu(n)
  players = create_players(game_board)
  winner_player = simulate(players, game_board)
  print(f"Vyhral hrac {winner_player}")


def get_user_input():
  field_size = 0
  error = False
  while field_size < 5:
    try:
      field_size = int(input("Zadajte velkost sachovnice(min. 5): "))
    except ValueError:
      print("\n[ValueError]: Prosim zadavajte iba cele cislo, skuste znova.")
      error = True
    except Exception:
      print("\n[Error]: Vyskytla nejaka chyba, prosim skuste znova.")
      error = True
    else:
      error = False
    if field_size < 5 and not error:
      print("\nPre zadane cislo nie je mozne vygenerovat sachovnicu...")
  
  if field_size % 2 == 0:
    print(f"\nCislo bolo upravene z {field_size} na {field_size-1}, aby " + 
          "bolo mozne vygenerovat sachovnicu.")
    field_size -= 1
  return field_size


def gensachovnicu(n):
  field = [[" " for _ in range(n)] for _ in range(n)]
  center = n // 2
  for row in range(n):
    for col in range(3):
      field[row][center-1+col] = ROAD_TILE
  for row in range(n):
    for col in range(3):
      field[center-1+col][row] = ROAD_TILE
  for row in range(1, n-1):
    field[row][center] = HOME_TILE
  for row in range(1, n-1):
    field[center][row] = HOME_TILE
  field[center][center] = BOARD_CENTER_TILE
  return field
  

def tlacsachovnicu(board):
  n_top_bar = [str(i) for i in range(len(board))]
  frame_buffer = "   " + " ".join(n_top_bar)
  for i in range(len(board)):
    frame_buffer += "\n"
    if i < 10:
      frame_buffer += f" {i}"
    else:
      frame_buffer += str(i)
    for j in range(len(board)):
      frame_buffer += f" {board[i][j]}"
  frame_buffer += "\n" + "---" * len(board)
  print(frame_buffer)


class Player:
  """ Instance of a player represents a player in the simulation. It has its own 
  start position, pawns and it is capable of handling them.
  
  :param n: size of the game board
  :param figure: character representing players figure
  :param start: tuple with a start pos and a direction vector
  -------------------------------------------------------------------------------
  Class variables,
  :var FIGURE {str}: figures character
  :var START {Vec2}: start position coordinates
  :var START_DIR {Vec2}: direction vector
  :var pawn_count {int}: max count of the players pawns
  :var pawns {list<dict>}: list of in-game pawns
  :var path {list<Vec2>}: preconstructed path, unique for every player 
  """  
  def __init__(self, n, figure, start):
    self.FIGURE = figure
    self.START = Vec2(start[0][0], start[0][1])
    self.START_DIR = Vec2(start[1][0], start[1][1])
    self.pawn_count = round((n - 3) / 2)
    self.pawns = []
    self.path = []

  def place_to_start(self, board):
    """ Place pawn to start position. If successful return True else False.
    
    :param board: 2d list representing the board
    :returns: operations success
    :rtype: bool
    """
    if self.is_pawn_at_start() == -1:
      self.log_kick_enemy(self.START, board)
      board[self.START.y][self.START.x] = self.FIGURE
      self.pawns.append(
        {
          "pos": Vec2(self.START.x, self.START.y),
          "path_index": 0
        }
      )
      print(f"Hrac {self.FIGURE} pridal panaka do hry.")
      return True
    return False

  def create_path(self, board):
    """ Generate the path for this player pawns and save it to self.path.
    
    :param board: 2d list game board
    """
    pos = self.START.copy()
    self.path.append(pos)
    forward = self.START_DIR.copy()
    for i in range(4):
      # Move forward
      for _ in range(self.pawn_count):
        pos.add(forward)
        self.path.append(pos.copy())
      forward.rotate(90, clockwise=True)  # Turn left
      # Move forward
      for _ in range(self.pawn_count):
        pos.add(forward)
        self.path.append(pos.copy())
      forward.rotate(90)  # Turn right
      if i < 3:
        # Move forward
        for _ in range(2):
          pos.add(forward)
          self.path.append(pos.copy())
        forward.rotate(90)  # Turn right
      else:
        # One step
        pos.add(forward)
        self.path.append(pos.copy())
        # Add home fields
        forward.rotate(90)
        for _ in range(self.pawn_count):
          pos.add(forward)
          self.path.append(pos.copy())
          
  def log_kick_enemy(self, pos, game_board):
    """ Check the position which is gonna be rewritten for enemy pawn.
    If at the given position is an enemy pawn, then log as kicked out pawn.

    :param pos: position to be checked
    :param game_board: 2d list representing the game_board
    """
    char_at_pos = game_board[pos.y][pos.x]  
    if (char_at_pos in PLAYER_FIGURES and
       char_at_pos != self.FIGURE):
      print(f"Hrac {self.FIGURE} vyhodil hraca {char_at_pos}.")

  def is_pawn_at_start(self):
    """ Check whether is pawn on start or not. If yes return index, otherwise -1.
    
    :returns: list index
    :rtype: int
    """
    for i in range(len(self.pawns)):
      if self.pawns[i]["pos"] == self.START:
        return i
    return -1

  def is_move_possible(self, path_index):
    """ Check whether on the given position is a friend pawn or not. 
    If yes return False, othewise True.
    
    :param move_pos: checked position
    :returns: whether a move can be executed
    :rtype: bool
    """
    for pawn in self.pawns:
      if pawn["path_index"] == path_index:
        return False
    if path_index >= len(self.path):
      return False
    return True

  def check_my_pawns(self, game_board):
    """ Monitoring the players pawns, if some pawns are missing it means that
    they were kick by an enemy player. So we remove those pawns from out listing.

    :param game_board: 2d list representing the board
    """
    remove_queue = []
    for pawn in self.pawns:
      if game_board[pawn["pos"].y][pawn["pos"].x] != self.FIGURE:
        remove_queue.append(pawn)
    for pawn in remove_queue:
      self.pawns.remove(pawn)

  def update_pawn(self, i_pawn, dice, game_board):
    """ Update the pawns position on the game board.
    
    :param i_pawn: index of the pawn in self.pawns
    :param dice: rolled number with the dice
    :param game_board: 2d list game board
    """
    # Reset old position
    old_pos = self.pawns[i_pawn].copy()
    house_fields = list(range(len(self.path)))[len(self.path)-self.pawn_count:]
    if old_pos["path_index"] in house_fields:
      game_board[self.pawns[i_pawn]["pos"].y][self.pawns[i_pawn]["pos"].x] = HOME_TILE
    else:
      game_board[self.pawns[i_pawn]["pos"].y][self.pawns[i_pawn]["pos"].x] = ROAD_TILE
    # Update pawns data
    pawns_path_index = self.pawns[i_pawn]["path_index"]
    self.pawns[i_pawn]["pos"] = self.path[pawns_path_index+dice]
    self.pawns[i_pawn]["path_index"] = pawns_path_index + dice
    # Log
    print(f"Hrac {self.FIGURE} posunul panaka z " +
       f"[{old_pos['pos'].x}, {old_pos['pos'].y}] " +
       f"na [{self.pawns[i_pawn]['pos'].x}, {self.pawns[i_pawn]['pos'].y}]")
    self.log_kick_enemy(self.pawns[i_pawn]["pos"], game_board)
    # Draw pawn to the board with new data
    game_board[self.pawns[i_pawn]["pos"].y][self.pawns[i_pawn]["pos"].x] = self.FIGURE

  def move_pawn(self, dice, game_board):
    """ Selects one of the pawns and move him according to the rules of the game.
    
    :param dice: rolled number with the dice
    :param game_board: 2d list game board
    """
    # Check if pawn is on start pos
    at_start = self.is_pawn_at_start()
    if at_start != -1:
      if self.is_move_possible(dice):
        self.update_pawn(at_start, dice, game_board)
        return
    # No pawn on start pos or couldnt move from start, so choose one
    tried = []
    pawn_indexes = list(range(len(self.pawns)))
    while len(tried) != len(self.pawns):
      i_chosen_pawn = choice(pawn_indexes)
      if self.is_move_possible(self.pawns[i_chosen_pawn]["path_index"] + dice):
        self.update_pawn(i_chosen_pawn, dice, game_board)
        break
      else:
        tried.append(i_chosen_pawn)
        pawn_indexes.remove(i_chosen_pawn)
    if len(tried) == len(self.pawns):
      print(f"Hrac {self.FIGURE} sa nedokaze pohnut, pokracuje dalsi hrac...")

  def is_winner(self):
    """ Check whether the house of this player is full or not.

    :rtype: str
    :returns: this players figure character
    """
    pawn_indexes = [i["path_index"] for i in self.pawns]
    path_len = len(self.path)
    house_pattern = list(range(path_len))[path_len-self.pawn_count:]
    return sorted(pawn_indexes) == house_pattern

  def __repr__(self):
    return f"Plyer_{self.FIGURE}"
      

class Vec2:
  """ 2D vector class, only with operations needed for this projects. """
  def __init__(self, x=0, y=0):
    if type(x) not in (int, float) or type(y) not in (int, float):
      raise ValueError("Vektor supporsts real numbers only.")
    self.x = x
    self.y = y

  def add(self, vector):
    if not isinstance(vector, Vec2):
      raise ValueError("Addend must be a vector.")
    self.x += vector.x
    self.y += vector.y

  def rotate(self, degree, clockwise=False):
    """ Rotates the vector clockwise/counterclockwise by the given angle."""
    current_x = self.x
    current_y = self.y
    angle = degree if not clockwise else 360-degree
    self.x = round(cos(radians(angle)) * current_x - sin(radians(angle)) * current_y)
    self.y = round(sin(radians(angle)) * current_x + cos(radians(angle)) * current_y)

  def copy(self):
    return Vec2(self.x, self.y)

  def __eq__(self, vector):
    return self.x == vector.x and self.y == vector.y

  def __repr__(self):
    return f"Vec2({self.x}, {self.y})"


def create_players(game_board):
  """ Creteate and initialize players. Their count depends on the
  global macro PLAYER_COUNT.

  :param game_board: 2d list representing the game board
  :rtype: list<Player>
  :returns: list of Player instances
  """
  n = len(game_board)
  # All the starting points and its directional vectors
  start_points = (
    ((n//2+1, 0), (0, 1)),
    ((n//2-1, n-1), (0, -1)),
    ((0, n//2-1), (1, 0)),
    ((n-1, n//2+1), (-1, 0))
  )
  # Create player
  players = []
  for p in range(PLAYER_COUNT):
    players.append(Player(n, PLAYER_FIGURES[p], start_points[p]))
  # Create paths for each player
  for player in players:
    player.create_path(game_board)
  return players


def play_with(player, game_board, debug=False):
  """ Takes a player and makes a move with him according to the given game boad 
  and rolled dice.

  :param player: participant of the simulated game, a Player instance
  :param board: 2d list representing the simulated games board
  :param debug: boolean value, if equals True the simulation can be stepped through
  """
  dice_state = 6
  player.check_my_pawns(game_board)
  while dice_state == 6:
    if debug:
      input("Stlac tlacitko pre pokracovanie...")
    dice_state = randint(1, 6)
    print(f"Hrac {player.FIGURE} hodil kockou cislo {dice_state}...")
    if dice_state == 6:
      if len(player.pawns) == player.pawn_count:
        # Pick one pawn and move him because there is no more unplaced pawn
        player.move_pawn(dice_state, game_board)
        tlacsachovnicu(game_board)
        if player.is_winner():
          return player.FIGURE
      else:
        # Place pawn to the start position if possible,
        # if not move the pawn from there
        place = player.place_to_start(game_board)
        if not place:
          player.move_pawn(dice_state, game_board)
        tlacsachovnicu(game_board)
        if player.is_winner():
          return player.FIGURE
    else:
      if len(player.pawns) != 0:
        # There are pawns on the board, so try to move one of them
        player.move_pawn(dice_state, game_board)
        tlacsachovnicu(game_board)
        if player.is_winner():
          return player.FIGURE
      else:
        # Current player has no pawns on the board
        print(f"Hrac {player.FIGURE} nema panaka v hre, pokracuje dalsi hrac...")
        tlacsachovnicu(game_board)


def simulate(players, game_board):
  """ Run simulations on a given set of players and a game board.

  :param players: list of Player instances
  :param game_board: 2d list representing the game board
  :rtype: str
  :returns: the winner players figure character
  """
  while True:
    for player in players:
      winner = play_with(player, game_board, debug=False)
      if winner:
        return winner


if __name__ == "__main__":
   main()

# ------------------------ Rozpis implementovanych pravidiel ------------------------ #
# 1. Keď padne šestka a hrac ma nevyuzitych panakov, musí daný hráč postaviť na svoju #
# štartovaciu pozíciu hracieho poľa svoju figúrku zo svojho domčeka (aj v prípade, ak #
# môže urobiť užitočný ťah s inou figúrkou), v pripade ze uz ma vsetkych panakov v    #
# hre, hrac si vyberie jedneho z panakov a postupi dalej. Potom môže znovu hádzať     #
# kockou a s danou figúrkou postúpiť daný počet polí dopredu.                         #
#                                                                                     #
# 2. Štartovacie pole sa musí uvoľniť čo najskôr, ako je možné.                       #
#                                                                                     #
# 3. Ak však hráč nemá v domčeku žiadnu figúrku, postúpi daný počet polí s figúrkou   #
# podľa svojej voľby vpred.                                                           #
#                                                                                     #
# 4. Ak sa stane že hráč je pred domčekom a potrebuje k výhre hodiť jedno jediné      #
# číslo a hráč hodí číslo 6 môže hádzať ešte raz.                                     #
#                                                                                     #
# 5. Keď padne číslo ktoré potrebuje a posledného panáčika umiestni do domčeka, stava #
# sa víťazom.                                                                         #
#                                                                                     #
# 6. Ak sa pri obehu po hracom poli dostane figúrka na pole, ktorá je obsadená        #
# figúrkou nepriateľa, nepriateľská figúrka sa musí vrátiť do domčeka (teda panak je  #
# odstraneny z hracieho pola a je priradeny k este nevyuzitim panakom)                #
#                                                                                     #
# 7. Vlastná figúrka nemôže "zbiť" svoju vlastnú figúrku a ak je cieľové pole         #
# obsadené vlastnou figúrkou, ťah je nevykonateľný. Hrac bud vykona pohyb inym        #
# panakom alebo poda dalsie kolo dalsiemu hracovi.                                    #
#                                                                                     #
# 8. Ak má hráč v obehu viac figúrok, môže sa rozhodnúť, ktorou potiahne. Hod kockami #
# v jednom kole jedným hráčom nesmie byť rozdelený medzi viac figúrok.                #
#                                                                                     #
# 9. Ak nemá hráč na hracom poli žiadnu figúrku (čo sa na začiatku hry týka každého   #
# hráča), musi hodit 6, aby mohol pridat panaka do hry na startovaciu poziciu.        #
# ----------------------------------------------------------------------------------- #