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

const getTest = () => {
  db.collection.find().toArray((err, items) => {
    console.log(items);
  });
};

const addSurvey = (data) => {
  MongoClient.connect(url, (err, client) => {
    const db = client.db("nodetest1");

    db.collection("usercollection").insertOne({ ...data });

    client.close();
  });
};

const data = {
  employeeId: 3,
  feedback: [
    { skillId: 1, rating: 2, description: "blahblah" },
    { skillId: 3, rating: 4, description: "hello" },
    { skillId: 4, rating: 5, description: "byebye" },
    { skillId: 2, rating: 4, description: "newdata" },
    { skillId: 6, rating: 3, description: "newestdata" },
    { skillId: 6, rating: 3, description: "newestdata2" },
  ],
};
addSurvey(data);

module.exports = { getVirtues, getVirtueBuckets, getEmployees };
