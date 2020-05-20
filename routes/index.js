module.exports = function (router, database) {
  router.get("/", (req, res) => {
    res.send({ response: "I am alive" }).status(200);
  });

  return router;
};
