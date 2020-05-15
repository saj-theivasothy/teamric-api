module.exports = function (router, database) {
  router.get("/", (req, res) => {
    database
      .getAllSurveys()
      .then((surveys) => res.send(surveys))
      .catch((err) => res.Error(err));
  });

  router.post("/", (req, res) => {
    database
      .addSurvey(req.data)
      .then((response) => res.send(response))
      .catch((err) => res.Error(err));
  });

  return router;
};
