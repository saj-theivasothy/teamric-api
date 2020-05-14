module.exports = function (router, database) {
  router.get("/", (req, res) => {
    database.getVirtues().then((virtues) => res.send(virtues));
  });

  router.get("/buckets", (req, res) => {
    database
      .getVirtueBuckets()
      .then((virtueBuckets) => res.send(virtueBuckets));
  });

  return router;
};
