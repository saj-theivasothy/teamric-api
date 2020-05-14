const express = require("express");
const app = express();
const server = require("http").createServer(app);
const io = require("socket.io")(server);

const cookieSession = require("cookie-session");
const bodyParser = require("body-parser");
const cors = require("cors");

const database = require("./data/database");

const indexRoutes = require("./routes/index");
const employeeRoutes = require("./routes/employee");
const surveyRoutes = require("./routes/survey");
const virtueRoutes = require("./routes/virtue");

const PORT = process.env.PORT || 8080;

app.use(
  cookieSession({
    name: "session",
    keys: ["key"],
  })
);

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));

app.use(
  cors({
    origin: function (origin, callback) {
      callback(null, true);
    },
    credentials: true,
  })
);

const indexRouter = express.Router();
indexRoutes(indexRouter, database);
app.use("/", indexRouter);

const employeeRouter = express.Router();
employeeRoutes(employeeRouter, database);
app.use("/employee", employeeRouter);

const surveyRouter = express.Router();
surveyRoutes(surveyRouter, database);
app.use("/survey", surveyRouter);

const virtueRouter = express.Router();
virtueRoutes(virtueRouter, database);
app.use("/virtues", virtueRouter);

server.listen(PORT, (err) => console.log(err || `listening on port ${PORT}`));
