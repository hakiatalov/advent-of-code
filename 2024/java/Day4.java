import java.io.IOException;

final String word = "XMAS"; // The word we are looking for
final int[][] directions = { // The different directions we want to traverse
  {0,1}, {0,-1}, {1,0}, {-1,0}, // Horizontal and vertical
  {1,1}, {1,-1}, {-1,1}, {-1,-1} // Diagonal
};

void main() throws IOException {
  int result = 0;
  
  // Get the file
  List<String> lines = Files.readAllLines(Path.of("inputs/day-4.txt"));
  
  // I want to be able to traverse the grid. So I need to know how many rows and columns there are. 
  // Rows are the number of lines. Columns are what? The length of the line. 

  int rows = lines.size();
  int columns = lines.get(0).length();

  // Create a grid for traversal.
  char[][] grid = new char[rows][columns];
  for (int i = 0; i < rows; i++) {
    grid[i] = lines.get(i).toCharArray(); // For each row take the row form the list. But convert it to a char array so that it fits the expected type of the grid. 
  }

  // Go through the grid, row by row, column by column, and see if there is a match

  // Iterate over the rows
  for (int r = 0; r < rows; r++) {
    // Iterate over the columns
    for (int c = 0; c < columns; c++) {
      // Check if there is a match for each starting character
      for (int[] d : directions) {
        if (match(grid, r, c, d[0], d[1])) {
          result++;
        }
      }
    }
  }

  IO.println("Part 1 result: " + result);
}

boolean match(char[][] grid, int rowStart, int columnStart, int rowDirection, int columnDirection) {
  // Here we want to start at some given index and then go into the provided direction.
  // At each point we check if the current index matches the index of the word.

  for (int i = 0; i < word.length(); i++) {
    int rr = rowStart + rowDirection * i;
    int cc = columnStart + columnDirection * i;

    // Check if out of bounds
    if (rr < 0 || rr >= grid.length || cc < 0 || cc >= grid[0].length) {
      return false;
    }

    // Check if match
    if (grid[rr][cc] != word.charAt(i)) {
      return false;
    }
  }
  return true;
}