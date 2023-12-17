function limitWords(sentence, limit) {
  if (sentence.length <= limit) {
    return sentence;
  }

  const words = sentence.split(" ");
  let truncatedString = "";
  let currentLength = 0;

  for (const word of words) {
    if (currentLength + word.length + 1 <= limit) {
      truncatedString += word + " ";
      currentLength += word.length + 1;
    } else {
      break;
    }
  }

  return truncatedString.trim();
}

function formatDate(date) {
  if (date) {
    return new Date(date).toISOString().split("T")[0];
  }
  return date;
}

export { limitWords, formatDate };
