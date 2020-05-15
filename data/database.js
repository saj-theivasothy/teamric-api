const db = require("./db/index.js");
const MongoClient = require("mongodb").MongoClient;
const url = "mongodb://localhost:27017";

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

const addSurvey = (data) => {
  MongoClient.connect(url, (err, client) => {
    const db = client.db("teamric");

    db.collection("surveys").insertOne({ ...data });

    client.close();
  });
};

const getAllSurveys = () => {
  return MongoClient.connect(url)
    .then((client) => {
      const database = client.db("teamric");
      const collection = database.collection("surveys");

      return collection.find().toArray();
    })
    .then((surveys) => {
      client.close();
      return surveys;
    });
};

module.exports = {
  getVirtues,
  getVirtueBuckets,
  getEmployees,
  getAllSurveys,
  addSurvey,
};
