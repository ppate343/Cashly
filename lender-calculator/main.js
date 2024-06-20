


//Purchase, Refinance or Renewal
//function route(type) {}

//function refinance(total_cost, income, mortgage_needed, property_value) {}

function ltv(mortgage_needed, property_value, mortgage_amount) {
  const current_ltv = (mortgage_amount / property_value) * 100;
  const new_ltv = ((mortgage_amount + mortgage_needed) / property_value) * 100;

  const lender = "";

  if (new_ltv > 80) {
    lender = "Private";
  } else {
    lender = 'ltv less than 80%, calculating GDS, TDS to determine'; 

   // if ltv < 8-, pop up gds tds calulate button to determine lender type
   // A & B will be later right now stick to private 

  }

  return 'Current LTV: ', current_ltv, 'New LTV: ', new_ltv, 'Lender Type: ', lender; 
}

function gds_tds_calculator(total_house_cost, total_cost, income) {
  const gds = (total_house_cost * 12) / income;
  const tds = (total_cost * 12) / income;

  return gds, tds;
}

function find_rates(ltv, fico) {

}
