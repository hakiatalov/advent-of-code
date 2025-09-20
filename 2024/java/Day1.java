record Pair(int left, int right) {}

void main() throws IOException {

  try (Stream<String> lines = Files.lines(Path.of("inputs/day-1.txt"))) {
    List<Pair> pairs = lines.map(line -> line.split("\\s+"))
                      .map(parts -> new Pair(Integer.parseInt(parts[0]), Integer.parseInt(parts[1])))
                      .toList();
    part1(pairs);
    part2(pairs);
  }
}

void part1(List<Pair> pairs) {
  List<Integer> lefts = pairs.stream().map(Pair::left).sorted().toList();
  List<Integer> rights = pairs.stream().map(Pair::right).sorted().toList();

  int result = IntStream.range(0, lefts.size()).map(i -> Math.abs(lefts.get(i) - rights.get(i))).sum();

  IO.println(result);
}

void part2(List<Pair> pairs) {
  List<Integer> lefts = pairs.stream().map(Pair::left).sorted().toList();
  List<Integer> rights = pairs.stream().map(Pair::right).sorted().toList();

  Map<Integer, Long> rightFrequency = rights.stream().collect(Collectors.groupingBy(n -> n, Collectors.counting()));

  long result = lefts.stream().mapToLong(n -> rightFrequency.getOrDefault(n, 0L) * n).sum();

  IO.println(result);
}
