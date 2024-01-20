import tkinter as tk
from tkinter import ttk, messagebox

class BlackjackStrategyGuide:
    def __init__(self, master):
        self.master = master
        self.master.title("Blackjack Strategy Guide")

        self.card_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

        # Player's Hand
        self.player_hand_label = tk.Label(master, text="Your Hand:")
        self.player_hand_label.pack(pady=5)

        self.player_hand_frame = tk.Frame(master)
        self.player_hand_frame.pack()

        self.player_hand_comboboxes = []
        self.add_card_combobox()
        self.add_card_combobox()

        self.add_card_button = tk.Button(master, text="Add Card", command=self.add_card_combobox, bg='#4CAF50', fg='white', font=('Helvetica', 12))
        self.add_card_button.pack(pady=10)

        # Dealer's Upcard
        self.dealer_upcard_label = tk.Label(master, text="Dealer's Upcard:")
        self.dealer_upcard_label.pack(pady=5)

        self.dealer_upcard = tk.StringVar()

        self.dealer_upcard_combobox = ttk.Combobox(master, textvariable=self.dealer_upcard, values=self.card_values, state="readonly", font=('Helvetica', 12))
        self.dealer_upcard_combobox.pack(pady=5)

        self.submit_button = tk.Button(master, text="Get Recommendation", command=self.get_recommendation, bg='#4CAF50', fg='white', font=('Helvetica', 12))
        self.submit_button.pack(pady=10)

    def add_card_combobox(self):
        card_var = tk.StringVar()
        combobox = ttk.Combobox(self.player_hand_frame, textvariable=card_var, values=self.card_values, state="readonly", font=('Helvetica', 12))
        combobox.pack(pady=5)
        self.player_hand_comboboxes.append((combobox, card_var))

    def get_recommendation(self):
        player_hand = [card_var.get() for _, card_var in self.player_hand_comboboxes if card_var.get()]
        dealer_upcard = self.dealer_upcard.get()

        if len(player_hand) < 2 or not dealer_upcard:
            messagebox.showwarning("Input Error", "Please select at least two cards for your hand and the dealer's upcard.")
            return

        recommendation = self.get_basic_strategy_recommendation(player_hand, dealer_upcard)
        messagebox.showinfo("Recommendation", recommendation)

    @staticmethod
    def get_basic_strategy_recommendation(player_hand, dealer_upcard):
        # Convert input to uppercase for case-insensitivity
        player_hand = [card.strip().upper() for card in player_hand]
        dealer_upcard = dealer_upcard.strip().upper()

        # Check for surrender
        if len(player_hand) == 2 and "A" in player_hand:
            if player_hand[1] == "8" and dealer_upcard in ["9", "10", "J", "Q", "K"]:
                return "Surrender"
            elif player_hand[1] == "7" and dealer_upcard == "10":
                return "Surrender"

        # Check for split
        if len(player_hand) == 2 and player_hand[0] == player_hand[1]:
            if player_hand[0] in ["A", "8"]:
                return "Always Split"
            elif player_hand[0] == "9" and dealer_upcard not in ["7", "10", "J", "Q", "K"]:
                return "Always Split"
            elif player_hand[0] == "7" and dealer_upcard not in ["8", "9", "10", "A"]:
                return "Split"
            elif player_hand[0] == "6" and dealer_upcard in ["2", "3", "4", "5", "6"]:
                return "Split"
            elif player_hand[0] == "5" and dealer_upcard not in ["5", "6"]:
                return "Double if possible, otherwise Hit"
            elif player_hand[0] == "4" and dealer_upcard in ["5", "6"]:
                return "Split"
            elif player_hand[0] == "3" and dealer_upcard in ["2", "3", "4", "5", "6"]:
                return "Split"
            elif player_hand[0] == "2" and dealer_upcard in ["2", "3", "4", "5", "6"]:
                return "Split"

        # Check for double
        if len(player_hand) == 2:
            if player_hand[0] == "A":
                return "Double if possible, otherwise Hit"
            elif player_hand[0] == "9" and dealer_upcard in ["3", "4", "5", "6"]:
                return "Double if possible, otherwise Stand"
            elif player_hand[0] == "8" and dealer_upcard in ["5", "6"]:
                return "Double if possible, otherwise Stand"
            elif player_hand[0] == "7" and dealer_upcard in ["3", "4", "5", "6"]:
                return "Double if possible, otherwise Hit"
            elif player_hand[0] == "6" and dealer_upcard in ["3", "4", "5", "6"]:
                return "Double if possible, otherwise Hit"
            elif player_hand[0] == "5" and dealer_upcard in ["4", "5", "6"]:
                return "Double if possible, otherwise Hit"
            elif player_hand[0] == "4" and dealer_upcard in ["4", "5", "6"]:
                return "Double if possible, otherwise Hit"
            elif player_hand[0] == "3" and dealer_upcard in ["5", "6"]:
                return "Double if possible, otherwise Hit"
            elif player_hand[0] == "2" and dealer_upcard in ["5", "6"]:
                return "Double if possible, otherwise Hit"

        # Check for hit or stand
        total_value = sum(card_value(card) for card in player_hand)
        if total_value >= 17:
            return "Stand"
        elif total_value == 16:
            if dealer_upcard in ["2", "3", "4", "5", "6"]:
                return "Stand"
            else:
                return "Hit"
        elif total_value == 15:
            if dealer_upcard in ["2", "3", "4", "5", "6"]:
                return "Stand"
            else:
                return "Hit"
        elif total_value == 14:
            if dealer_upcard in ["2", "3", "4", "5", "6"]:
                return "Stand"
            else:
                return "Hit"
        elif total_value == 13:
            if dealer_upcard in ["2", "3", "4", "5", "6"]:
                return "Stand"
            else:
                return "Hit"
        elif total_value == 12:
            if dealer_upcard in ["4", "5", "6"]:
                return "Stand"
            else:
                return "Hit"
        elif total_value == 11:
            return "Double if possible, otherwise Hit"
        elif total_value == 10:
            if dealer_upcard in ["2", "3", "4", "5", "6", "7", "8", "9"]:
                return "Double if possible, otherwise Hit"
            else:
                return "Hit"
        elif total_value == 9:
            if dealer_upcard in ["3", "4", "5", "6"]:
                return "Double if possible, otherwise Hit"
            else:
                return "Hit"
        else:
            return "Hit"

def card_value(card):
    if card in ['K', 'Q', 'J']:
        return 10
    elif card == 'A':
        return 11
    else:
        return int(card)

if __name__ == "__main__":
    root = tk.Tk()
    app = BlackjackStrategyGuide(root)
    root.mainloop()
