const express = require("express");
const cookieSession = require("cookie-session");
const bodyparser = require("body-parser");
const cors = require("cors")

const indexRoutes = require("./routes/index");
const userRoutes = require("./routes/users");
const surveyRoutes = require("./routes/survey")

const app = express();
const port = "8080";

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

const userRouter = express.Router();
userRoutes(userRouter, database);
app.use("/user", userRouter);

const surveyRouter = express.Router();
surveyRoutes(surveyRouter, database);
app.use("/survey", surveyRouter);

app.listen(port, (err) => console.log(err || `listening on port ${port}`));

