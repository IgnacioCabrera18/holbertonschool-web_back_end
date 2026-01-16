function cleanSet(set, startString) {
  const result = [];

  for (const value of set) {
    if (value.startsWith(startString)) {
      const remainder = value.substring(startString.length);
      result.push(remainder);
    }
  }

  return result.join('-');
}
