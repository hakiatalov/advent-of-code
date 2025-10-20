import java.util.stream.IntStream;

void main() throws IOException {
 try (Stream<String> lines = Files.lines(Path.of("inputs/day-2.txt"))) {
    List<List<Integer>> reports = lines.map(line -> line.split("\\s+"))
      .map(parts -> Arrays.stream(parts).map(Integer::parseInt).toList())
      .toList();

    part1(reports);
    part2(reports);
  }
}

void part1(List<List<Integer>> reportList) {
  long count = reportList.stream()
        .filter(this::isSafePart1)
        .count();

  IO.println("Part 1 safe reports: " + count);
}

void part2(List<List<Integer>> reportList) {
  long count = reportList.stream()
        .filter(this::isSafePart2)
        .count();
  
  IO.println("Part 2 safe reports: " + count);
}

boolean isSafePart1(List<Integer> report) {

  List<Integer> diffs = IntStream.range(0, report.size() - 1)
                              .map(i -> report.get(i + 1) - report.get(i))
                              .boxed()
                              .toList();

  if (diffs.isEmpty()) {
    return false;
  }

  boolean allIncreasing = diffs.stream().allMatch(d -> d >= 1 && d <= 3);
  boolean allDecreasing = diffs.stream().allMatch(d -> d <= -1 && d >= -3);
  
  return allIncreasing || allDecreasing;
}

boolean isSafePart2(List<Integer> report) {
  if (isSafePart1(report)) {
    return true;
  }

  for (int i = 0; i < report.size(); i++) {
    List<Integer> modified = new ArrayList<>(report);
    modified.remove(i);
    if (isSafePart1(modified)) {
      return true;
    }
  }

  return false;
}