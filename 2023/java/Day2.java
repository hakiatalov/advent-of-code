import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Map;
import java.util.Optional;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Stream;

class Day2 {

  public static void main(String[] args) {
    
    Path path = Path.of("inputs/day2.txt");

    int part1 = 0;
    int part2 = 0;

    try (Stream<String> lines = Files.lines(path)) {
      part1 = lines.mapToInt(Day2::isGamePossible).sum();   
    } catch (IOException e) {
      e.printStackTrace();
    }

    try (Stream<String> lines = Files.lines(path)) {
      part2 = lines.mapToInt(Day2::getCubePower).sum();   
    } catch (IOException e) {
      e.printStackTrace();
    }

    System.out.println("Part 1: " + part1);
    System.out.println("Part 2: " + part2);

  }

  public static int getCubePower(String line) {

    String redRegex = "\\d+(?= red)";
    String greenRegex = "\\d+(?= green)";
    String blueRegex = "\\d+(?= blue)";

    var maxRed = Pattern.compile(redRegex).matcher(line).results().map(r -> Integer.parseInt(r.group())).max(Integer::compare).orElse(0);
    var maxGreen = Pattern.compile(greenRegex).matcher(line).results().map(r -> Integer.parseInt(r.group())).max(Integer::compare).orElse(0);
    var maxBlue = Pattern.compile(blueRegex).matcher(line).results().map(r -> Integer.parseInt(r.group())).max(Integer::compare).orElse(0);

    
    return maxRed * maxGreen * maxBlue;
  }

  public static int isGamePossible(String line) {

    final var colorMap = Map.of(
      "red", 12,
      "green", 13,
      "blue", 14
    );

    String gameNumberRegex = "\\d+(?=:)";
    String redRegex = "\\d+(?= red)";
    String greenRegex = "\\d+(?= green)";
    String blueRegex = "\\d+(?= blue)";

    String gameNumber = Pattern.compile(gameNumberRegex).matcher(line).results().findFirst().get().group();

    boolean isRed = Pattern.compile(redRegex).matcher(line).results().allMatch(e -> Integer.parseInt(e.group()) <= colorMap.get("red"));
    boolean isGreen = Pattern.compile(greenRegex).matcher(line).results().allMatch(e -> Integer.parseInt(e.group()) <= colorMap.get("green"));
    boolean isBlue = Pattern.compile(blueRegex).matcher(line).results().allMatch(e -> Integer.parseInt(e.group()) <= colorMap.get("blue"));

    return isRed && isGreen && isBlue ? Integer.parseInt(gameNumber) : 0;
  }

}
