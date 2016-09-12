angular.module('opal.controllers').controller('AddPatient',
  function(scope, step, episode) {
    "use strict";
    scope.drugs = [
      "Rifampicin",
      "Isoniazid",
      "Pyrazinamide",
      "Ethambutol",
      "Moxifloxacin",
      "Levofloxacin",
      "Amikacin",
      "Kanamycin",
      "Capreomycin"
    ];
});
