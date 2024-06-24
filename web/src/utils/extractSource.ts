export default function extractSource(input: string): string {
  if (!input) return "";

  const split = input.split("-");

  if (split.length > 0) {
    return split[1];
  } else {
    return "";
  }
}
