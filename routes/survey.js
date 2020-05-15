module.exports = function (router, database) {
  router.get("/", (req, res) => {
    database
      .getAllSurveys()
      .then((surveys) => {
        res.send(surveys)})
      .catch((err) => {
        res.send(err)});
  });

  router.post("/", (req, res) => {
    database
      .addSurvey(req.body.data)
      .then((response) => res.send(response))
      .catch((err) => res.send(err));
  });

  return router;
};
