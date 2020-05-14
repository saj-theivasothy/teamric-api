const db = require("./db/index.js");

const getVirtues = () => {
  const queryString = `
    SELECT * FROM virtues;
    `;

  return db.query(queryString).then((res) => res.rows);
};

const getVirtueBuckets = () => {
  const queryString = `
        SELECT * FROM virtue_buckets;
    `;

  return db.query(queryString).then((res) => res.rows);
};

const getEmployees = () => {
  const queryString = `
    SELECT * FROM employees;
  `;

  return db.query(queryString).then((res) => res.rows);
};

module.exports = { getVirtues, getVirtueBuckets };
