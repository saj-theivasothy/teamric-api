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
  return MongoClient.connect(url)
  .then((client) => {
    const database = client.db("teamric");

    return database.collection("surveys").insertOne({ ...data });
    client.close();
  })
  .then((res) => {
    return res;
  })
};

const getAllSurveys = () => {
  return MongoClient.connect(url)
    .then((client) => {
      const database = client.db("teamric");
      const collection = database.collection("surveys");

      return collection.find().toArray();
      client.close();
    })
    .then((surveys) => {
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
