const db = require("./db/index.js");

const getVirtues = () => {
  const queryString = `
    SELECT * FROM virtues;
    `;

  return db.query(queryString).then((res) => res.rows);
};

getVirtues();
