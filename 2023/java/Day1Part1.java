import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Stream;

class Day1Part1 {

  static Map<String, String> digitMap = Map.of(
    "one", "1",
    "two", "2",
    "three", "3",
    "four", "4",
    "five", "5",
    "six", "6",
    "seven", "7",
    "eight", "8",
    "nine", "9",
    "zero", "0"
  );
 
  public static void main(String[] args) {
    
    var part1 = 0;
    var part2 = 0;

    Path path = Path.of("inputs/day-1.txt");
    // Path path = Path.of("inputs/day-1-test.txt");

    try (Stream<String> lines = Files.lines(path)) {
      part1 = lines.mapToInt(line -> extractFirstAndLastDigitsPart1(line)).sum();
    } catch (IOException e) {
      e.printStackTrace();
    }

    try (Stream<String> lines = Files.lines(path)) {
      part2 = lines.mapToInt(line -> extractFirstAndLastDigitsPart2(line)).sum();
    } catch (IOException e) {
      e.printStackTrace();
    }

    System.out.printf("Part 1: %s%n", part1);
    System.out.printf("Part 2: %s%n", part2);

  }

  public static Integer extractFirstAndLastDigitsPart1(String line) {
    String regex = "\\d"; // Define the regular expression

    Pattern pattern = Pattern.compile(regex);
    Matcher matcher = pattern.matcher(line);
    String first = "";
    String last = "";

    List<String> matchResult = matcher.results().map(e -> e.group()).toList();

    if (!matchResult.isEmpty()) {
      first = matchResult.get(0);
      last = matchResult.get(matchResult.size() - 1);
    }

    if (!first.isEmpty() || !last.isEmpty()) {
      return Integer.parseInt(first + last);
    } else {
      return 0;
    }
  }


  public static Integer extractFirstAndLastDigitsPart2(String line) {
    Set<String> keySet = digitMap.keySet();
    String regex = "(" + String.join("|", keySet) + "|\\d)"; // Define the regular expression
    
    Pattern pattern = Pattern.compile(regex);
    Matcher matcher = pattern.matcher(line);
    String first = "";
    String last = "";

    List<String> matchResult = new ArrayList<String>();

    int start = 0;
    while (matcher.find(start)) {
      matchResult.add(matcher.group());
      start = matcher.start() + 1;  // Move to the next character after the start of the match
    }

    if (!matchResult.isEmpty()) {
      first = digitMap.containsKey(matchResult.get(0)) ? digitMap.get(matchResult.get(0)) : matchResult.get(0);
      last =  digitMap.containsKey(matchResult.get(matchResult.size() - 1)) ? digitMap.get(matchResult.get(matchResult.size() - 1)) : matchResult.get(matchResult.size() - 1);
    }

    return Integer.parseInt(first + last);
  }
}
