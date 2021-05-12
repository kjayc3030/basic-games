/**
 * @author Kean Jaycox
 * 5/12/2021
 * This is a game of Tic Tac Toe versus another player. Player one is 'X'
 * while player two is 'O'. There are nine turns total with player one starting.
 */

import java.util.Scanner;

public class PvPTicTacToe {

	public static String[] board = new String[9];
	
	// Prints formatted board with existing values
	public static void printBoard() {
		for(int i = 0; i < 9; i++) {
			if(i == 2 || i == 5 || i == 8)
				System.out.println(board[i]);
			else
				System.out.print(board[i]);
		}
	}
	
	// Populates board with empty spaces to begin game
	public static void populateBoard() {
		for(int i = 0; i < 9; i++) {
			board[i] = "[ ]";
		}
	}
	
	// Player choices, uses recursion if position already in use
	public static void playerOneChoice(String[] board, Scanner scn) {
		int choice = scn.nextInt();
		if(board[choice-1] == "[ ]")
			board[choice-1] = "[X]";
		else {
			System.out.println("Spot already taken, please choose another");
			playerOneChoice(board, scn);
		}
	}
	
	public static void playerTwoChoice(String[] board, Scanner scn) {
		int choice = scn.nextInt();
		if(board[choice-1] == "[ ]")
			board[choice-1] = "[O]";
		else {
			System.out.println("Spot already taken, please choose another");
			playerTwoChoice(board, scn);
		}
	}
	
	// checkWin methods return true if someone lines up three scores
	public static boolean checkPlayerOneWin(String[] board) {
		if(board[0] == "[X]" && board[1] =="[X]" && board[2] == "[X]") {return true;}
		if(board[0] == "[X]" && board[4] =="[X]" && board[8] == "[X]") {return true;}
		if(board[0] == "[X]" && board[3] =="[X]" && board[6] == "[X]") {return true;}
		if(board[1] == "[X]" && board[4] =="[X]" && board[7] == "[X]") {return true;}
		if(board[2] == "[X]" && board[5] =="[X]" && board[8] == "[X]") {return true;}
		if(board[2] == "[X]" && board[4] =="[X]" && board[6] == "[X]") {return true;}
		if(board[3] == "[X]" && board[4] =="[X]" && board[5] == "[X]") {return true;}
		if(board[6] == "[X]" && board[7] =="[X]" && board[8] == "[X]") {return true;}
		else {return false;}
	}
	
	public static boolean checkPlayerTwoWin(String[] board) {
		if(board[0] == "[O]" && board[1] =="[O]" && board[2] == "[O]") {return true;}
		if(board[0] == "[O]" && board[4] =="[O]" && board[8] == "[O]") {return true;}
		if(board[0] == "[O]" && board[3] =="[O]" && board[6] == "[O]") {return true;}
		if(board[1] == "[O]" && board[4] =="[O]" && board[7] == "[O]") {return true;}
		if(board[2] == "[O]" && board[5] =="[O]" && board[8] == "[O]") {return true;}
		if(board[2] == "[O]" && board[4] =="[O]" && board[6] == "[O]") {return true;}
		if(board[3] == "[O]" && board[4] =="[O]" && board[5] == "[O]") {return true;}
		if(board[6] == "[O]" && board[7] =="[O]" && board[8] == "[O]") {return true;}
		else {return false;}
	}

	public static void main(String args[]) {
		
		Scanner scn = new Scanner(System.in);
		
		populateBoard();
		// Introduce game and simple instructions
		System.out.println("Player one is 'X', player two is 'O'\nPlayer one select position 1-9 to begin");
		System.out.print("[1][2][3]\n[4][5][6]\n[7][8][9]\n");
		
		for(int i = 0; i < 9; i++) {
			if ((i % 2) == 0) {					// gives turn to player one or two
				playerOneChoice(board, scn);	// passes board & scanner for choice
				printBoard();					// prints board after each player turn
				if(checkPlayerOneWin(board)) {
					System.out.print("Player one wins!");
					System.exit(1);							
				}
			}
			else {
				playerTwoChoice(board, scn);
				printBoard();
				if(checkPlayerTwoWin(board)) {
					System.out.print("Player two wins");
					System.exit(1);
				}
			}
		}
		System.out.print("Game Over");
	}
}