/*
 * Go through each line an identify the correct multiply instructions. 
 * A correct instruction must look like this: mul(x,y) where x and y are digits between 1 and 3 characters
 * Find the matching string. For each match, extract the two numbers and find the product. Add the product to the result.
 */

import java.io.IOException;

void main() throws IOException {
  Path path = Path.of("inputs/day-3.txt");
  IO.println("Part 1 result: " + part1(path));
  IO.println("Part 2 result: " + part2(path));
}

long part1(Path path) throws IOException {
  long sum = 0;
  String s = Files.readString(path);
  Pattern p = Pattern.compile("mul\\((\\d+),(\\d+)\\)"); // This gives me three groups. Group 0 = full match, group 1 = first integer, group 2 = second integer
  Matcher m = p.matcher(s);
  
  while(m.find()) {
    int x = Integer.parseInt(m.group(1));
    int y = Integer.parseInt(m.group(2));
    sum += (long) x * y;
  }

  return sum;
}

long part2(Path path) throws IOException {
  long sum = 0;
  boolean enabled = true;

  String s = Files.readString(path);
  Pattern p = Pattern.compile("do\\(\\)|don't\\(\\)|mul\\((\\d+),(\\d+)\\)");
  Matcher m = p.matcher(s);

  while(m.find()) {
    if (m.group().equals("do()")) {
      enabled = true;
    } else if (m.group().equals("don't()")) {
      enabled = false;
    } else {
      int x = Integer.parseInt(m.group(1));
      int y = Integer.parseInt(m.group(2));
      sum += enabled ? (long) x * y : 0;
    }
  }

  return sum; 
}