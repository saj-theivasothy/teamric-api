module.exports = function (router, database) {
  router.get("/", (req, res) => {
    database.getEmployees().then((employees) => res.send(employees));
  });

  return router;
};
