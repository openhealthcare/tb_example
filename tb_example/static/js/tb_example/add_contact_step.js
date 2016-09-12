angular.module('opal.controllers').controller('AddContact',
  function(scope, step, episode) {
    "use strict";
    scope.symptoms = [
      "Cough",
      "Fever",
      "Weight Loss",
      "Sweats",
      "Other"
    ];

    scope.drugs = [
      "Rifampicin",
      "Isoniazid",
      "Rifinah",
      "Levofloxacin",
      "Other"
    ];
});
