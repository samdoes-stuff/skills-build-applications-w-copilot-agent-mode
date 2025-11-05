/**
 * Formats a column name by replacing underscores with spaces and capitalizing each word.
 * @param {string} columnName - The column name to format
 * @returns {string} The formatted column name
 */
export const formatHeader = (columnName) => {
  return columnName.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase());
};
