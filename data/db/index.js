const { Pool } = require("pg");

// creates a connection with psql database
const pool = new Pool({
  user: "vagrant",
  password: "123",
  host: "localhost",
  database: "teamric",
});

module.exports = {
  query: (text, params) => {
    return pool.query(text, params);
  },
};
