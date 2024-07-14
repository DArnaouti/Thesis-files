#python 3.6.9  

 
import re  


def merge_numeric_items_in_preconditions(input_list):  

    merged_dict = {}  

    # Initialize a list to store non-numeric items  

    non_num_list = []  

    # Iterate over each item in the input list  

    for item in input_list:  

        # Check if the item contains any comparison operators  

        if not any(op in item for op in ['>=', '<=', '=', '<', '>']):  

            non_num_list.append(item)  # Append non-numeric items to the list  

            continue  # Skip processing for non-numeric items  

        # Extract operator, predicate, and value using regular expressions  

        match = re.match(r'\((>=|<=|=|<|>) \((.*?)\) (\d+)\)', item)  

        if match:  

            operator = match.group(1)  

            predicate = match.group(2)  

            value = int(match.group(3))  

            # Add the value to the corresponding key in the dictionary  

            if (operator, predicate) in merged_dict:  

                merged_dict[(operator, predicate)] += value  

            else:  

                merged_dict[(operator, predicate)] = value  

        else:  

            non_num_list.append(item)  # Append non-matching items to the list  

  
    # Create a list to store the merged items  

    merged_items = []  

    # Iterate over the items in the merged dictionary  

  
    for (operator, predicate), value in merged_dict.items():  

        # Construct the merged item and add it to the list  

        merged_item = f'({operator} ({predicate}) {value})'  

        merged_items.append(merged_item)  

  
    # Return the merged items along with the non-numeric items  

    return set(merged_items + non_num_list)  

  

   

  

def replace_variables_if_hirarchy(list1, list2):  

    replaced1 = ""  

    replaced2 = ""  

    for i, item1 in enumerate(list1):  

        for item2 in list2:  

            left_subitem1 = item1.split(' ')[1]  # Extract the left sub-item from list1  

            left_subitem2 = item2.split(' ')[1]  # Extract the left sub-item from list2  

  
            if left_subitem1 == left_subitem2:  

                replaced1 = item1.split(' ')[-1].strip('()')  

                replaced2 = item2.split(' ')[-1].strip('()')  

                list1[i] = item1.replace(item1.split(' ')[-1].strip('()'), item2.split(' ')[-1].strip('()'))  # Replace the right sub-item in list1  

                break  

    for i, item1 in enumerate(list1):  

        for item2 in list2:  

            left_subitem1 = item1.split(' ')[1]  # Extract the left sub-item from list1  

            left_subitem2 = item2.split(' ')[1]  # Extract the left sub-item from list2  

            if item1.split(' ')[-1].strip('()') == replaced1 and item2.split(' ')[-1].strip('()') == replaced2:  

                list1[i] = item1.replace(item1.split(' ')[-1].strip('()'), item2.split(' ')[-1].strip('()'))  # Replace the right sub-item in list1  

    return list1  

  

def parameters_has_common_values(list1, list2):  

    for item in list1:  

        if item in list2:  

            continue  

        value = item.split('-')[1].strip()  

        if value in [x.split('-')[1].strip() for x in list2]:  

            return True  

    return False  

  

   


def do_numeric_calculations(ab):
  """
  Merges numeric effects with the same fluents in three lists.

  Args:
      a_effects: A list of effects for agent A.
      b_effects: A list of effects for agent B.
      ab_effects: A list of combined effects.

  Returns:
      A list of merged effects in ab.effects.
  """
  result = None  
  pattern = ""  
  increase_pattern = r"\(increase \((.*?)\) (\d+)\)"  
  decrease_pattern = r"\(decrease \((.*?)\) (\d+)\)"  
  for i, item1 in enumerate(ab):  # Iterate over a copy to avoid modifying original list
    match1_increase = re.match(increase_pattern, item1)
    match1_decrease = re.match(decrease_pattern, item1)
    if match1_increase:  


            operation1 = match1_increase.group(1)  

            value1 = int(match1_increase.group(2)) 

            for j, item2 in enumerate(ab):  

                match2_increase = re.match(increase_pattern, item2)  

                match2_decrease = re.match(decrease_pattern, item2)

                if match2_increase:
                   
                   operation2 = match2_increase.group(1)  

                   value2 = int(match2_increase.group(2))  

                   if operation1 == operation2 and i != j:  
                        print(operation1)
                        print(operation2)
                        sum_value = value1 + value2  
                        print(sum_value)
                        result = f"(increase ({operation1}) {sum_value})" 
                        print(result) 
                        ab.remove(item1)
                        ab.remove(item2)
                        ab.append(result)
                        break  
                elif match2_decrease:

                   operation2 = match2_decrease.group(1)  

                   value2 = int(match2_decrease.group(2))  

                   if operation1 == operation2 and i != j:  

                        if value1 > value2:  

                            pattern = "increase"  

                        elif value1 < value2:  

                            pattern = "decrease"  

                        elif value1 == value2:
                           ab.remove(item1)
                           ab.remove(item2)
                           break 

                        diff_value = abs(value2 - value1)
                        result = f"({pattern} ({operation1}) {diff_value})"
                        ab.remove(item1)
                        ab.remove(item2)
                        ab.append(result)
                        break  
                   

    elif match1_decrease:  

            operation1 = match1_decrease.group(1)  

            value1 = int(match1_decrease.group(2))  

            for j, item2 in enumerate(ab):  

                match2_increase = re.match(increase_pattern, item2)  

                match2_decrease = re.match(decrease_pattern, item2)  

                if match2_increase:  

                    operation2 = match2_increase.group(1)  

                    value2 = int(match2_increase.group(2))  

                    if operation1 == operation2 and i != j:  

                        if value1 < value2:  

                            pattern = "increase"  

                        elif value1 > value2:  

                            pattern = "decrease"  

                        elif value1 == value2:
                            
                           ab.remove(item1)
                           ab.remove(item2)
                           break  

                              

                        diff_value = abs(value2 - value1)  # Subtract the greater value from the smaller value  

                        result = f"({pattern} ({operation1}) {diff_value})"  
                        ab.remove(item1)
                        ab.remove(item2)
                        ab.append(result)
                        
                        break  

                elif match2_decrease:  

                    operation2 = match2_decrease.group(1)  

                    value2 = int(match2_decrease.group(2))  

                    if operation1 == operation2 and i != j:  
                        sum_value = value1 + value2  
                        result = f"(decrease ({operation1}) {sum_value})"  
                        ab.remove(item1)
                        ab.remove(item2)
                        ab.append(result)
                        break  
               
  return ab

  

  

   

  

def has_different_variable_names(list1, list2):  

    for item2 in list2:  

        variable2 = item2.split(' - ')[0]  

        value2 = item2.split(' - ')[1]  

        for item1 in list1:  

            variable1 = item1.split(' - ')[0]  

            if value2 in item1 and variable2 != variable1 and len(variable2) <= 3:  

               return True  

    return False  

  
  

   

  

def update_variables_names_in_precondition_and_effects(dict1, dict2):  

    # Extract values and variables from the dictionaries  

    variables1 = [param.split(' - ')[0] for param in dict1['parameters'] if ' - ' in param]  

    values1 = [param.split(' - ')[1] for param in dict1['parameters'] if ' - ' in param]  

    variables2 = [param.split(' - ')[0] for param in dict2['parameters'] if ' - ' in param]  

    values2 = [param.split(' - ')[1] for param in dict2['parameters'] if ' - ' in param]  

    variables3 = [item for item in variables2 if len(item) <= 2]  

    index = variables2.index(variables3[0])  

    values3 = values2[index]  

    replaced_var = None  

    for element in dict1['parameters']:  

        if values3 in element:  

            replaced_var = element.split(' - ')[0]  

            break  

    # Find values that appear with multiple variables  

    all_values = values1 + values2  

    shared_values = set([value for value in all_values if all_values.count(value) > 1])  

    # Update variables in dict2  

    selected_variables = [var3.split(' - ')[0] for var3 in variables3]  

    dict2_params = [pa.split(' - ')[0] for pa in dict2['parameters']]  

    for i in range(len(selected_variables)):  

        if selected_variables[i] not in dict2_params:  

            continue  

        value = values2[i]  

        if value in shared_values and selected_variables[i] != variables1[values1.index(value)]:  

            dict2['parameters'][i] = dict2['parameters'][i].replace(selected_variables[i], variables1[values1.index(value)])  

    dict2['precondition'] = [item.replace(variables3[0], replaced_var) for item in dict2['precondition']]  

    dict2['effect'] = [item.replace(variables3[0], replaced_var) for item in dict2['effect']]  

    return dict2  

  

   

  

   

  

   

  

def correct_effects(a,b):  

    filtered_list = []  

    for item in a:  

        if item.startswith('(not '):  

            opposite_item = item[5:-1]  

        else:  

            opposite_item = '(not (' + item[1:-1] + '))'  

        if opposite_item not in b:  

            filtered_list.append(item)  

    return (filtered_list)  

  

   

  

   

  

def has_duplicate_vars(lst):  

    var_set = set()  

    for item in lst:  

        var = item.split(' - ', 1)[0]  

        if var in var_set:  

            return True  

        var_set.add(var)  

    return False  

  

   

  

def modify_parameters(lst):  

    item_dict = {}  

    for item in lst:  

        var_value, value = item.split(' - ', 1)  

        if value in item_dict:  

            if len(var_value) > len(item_dict[value]):  

                item_dict[value] = var_value  

        else:  

            item_dict[value] = var_value  

    return [f"{var_value} - {value}" for value, var_value in item_dict.items()]  

  

   

  

   

  

def has_multi_vars(lst):  

    for item in lst:  

        if item.count("?") > 1:  

            return True  

    return False  

  

def find_multi_variables(list1):  

    for item in list1:  

        if "-" in item:  

            variables = item.split("-")[0].strip().split(" ")  

            if len(variables) > 1:  

                value = item.split("-")[1].strip().split(" ")  

                new_var = item.split()[0]   


    return (value, new_var)  

  

   

  

def mutate_the_dict(value, new_variable, my_dict):  

    for i, param in enumerate(my_dict["parameters"]):  

        if value in param:  

            my_dict["parameters"][i] = param.replace(value, new_variable)  


    for j, precond in enumerate(my_dict["precondition"]):  

        if value in precond:  

            my_dict["precondition"][j] = precond.replace(value, new_variable)  

    for k, effect in enumerate(my_dict["effect"]):  

        if value in effect:  

            my_dict["effect"][k] = effect.replace(value, new_variable)  


    return my_dict  

  

   

  

def extract_variables(list1, list2, item):  

    variable_set = []  

    for lst in [list1, list2]:  

        for element in lst:  

            components = element.split('-')  

            if len(components) > 1 and item in components[1]:  

                variables = [var.strip() for var in components[0].split()]  

                if len(variables) > 0:  

                    variable_set.append(variables[0])  

    variable_set.sort(key=len)                

    return tuple(variable_set)  

  

   

  

# Check if some variables in both lists have the same name  

  

def update_variable_names(old_list):  

    variables = []  

    new_list = []  

    updated_pre_eff = []  


    for item in old_list:  

        variable, value = item.split(' - ')  

        # Check if there are multiple variables in the item  

        if " " in variable:  

            multi_variables = variable.split(" ")  

            variables.extend(multi_variables)  

            new_item = f'{multi_variables} - {value}'  

            new_list.append(new_item)  

        else:  

            if variable in variables:  

                updated_pre_eff.append(variable)  

                variable = variable + "1"  

                edited_value = value  

            variables.append(variable)             

            new_item = f'{variable} - {value}'  

            new_list.append(new_item)  

    if any(item in element for element in a["parameters"]):   

        for x in updated_pre_eff:  

            a["precondition"] = update_sub_item(a["precondition"], x)  

            a["effect"] = update_sub_item(a["effect"], x)      


    if any(item in element for element in b["parameters"]):   

        for x in updated_pre_eff:  

            b["precondition"] = update_sub_item(b["precondition"], x)  

            b["effect"] = update_sub_item(b["effect"], x)      

    return new_list  

  

# Updates preconditions and effects with new parameter variable names.  

  

def update_sub_item(list1, sub_item):  

    for i in range(len(list1)):  

        if sub_item in list1[i]:  

            updated_item = list1[i].replace(sub_item, sub_item + "1")  

            list1[i] = updated_item  

    return list1  

  

   

  

   

  

   

def generate_macro_action(a, b):  

 
    need_modifying_parameters = False  

    if parameters_has_common_values(a["parameters"], b["parameters"]):  

  
        if has_multi_vars(a["parameters"]):  

            need_modifying_parameters = True  

            multi = find_multi_variables(a["parameters"])  

            extracted_vars = extract_variables(a["parameters"], b["parameters"], multi[0][0])  

            b = mutate_the_dict(extracted_vars[0], extracted_vars[1], b)  

        if has_multi_vars(b["parameters"]):  

            need_modifying_parameters = True  

            multi = find_multi_variables(b["parameters"])  

            extracted_vars = extract_variables(a["parameters"], b["parameters"], multi[0][0])  

            a = mutate_the_dict(extracted_vars[0], extracted_vars[1], a)  

    def num_effects(effnum):  

        return {eff for eff in effnum if "increase" in eff or "decrease" in eff}  

  
   
    ab = {}  

    # Step 1  

    ab["name"] = a["name"] + "-" + b["name"]  

    # Step 2  

    if has_duplicate_vars(list(dict.fromkeys(a["parameters"] + b["parameters"]))):  

            ab["parameters"] = update_variable_names(list(dict.fromkeys(a["parameters"] + b["parameters"])))  

  
    else:  

            ab["parameters"] = list(dict.fromkeys(a["parameters"] + b["parameters"]))  

    if need_modifying_parameters:  

        ab["parameters"] = modify_parameters(ab["parameters"])  

    # Step 3  

    if has_different_variable_names(a["parameters"], b["parameters"]):  

        update_variables_names_in_precondition_and_effects(a, b)  

    

    ab["precondition"] = []  

  
    # propositional preconditions
    modified = [item for item in b["precondition"] if item not in a["effect"]]  

    

    ab["precondition"] = modified + a["precondition"]  

  
    ab["precondition"] = merge_numeric_items_in_preconditions(ab["precondition"])  

    ab["effect"] = []  

  

    for num_eff in b["effect"]:  

            ab["effect"].append(num_eff)  

  
    for num_eff in a["effect"]:  

        # Exclude the effects of a that are in the negative effects of b  

            ab["effect"].append(num_eff)  

    # propositional effects
    ab["effect"] = correct_effects(ab["effect"], b["effect"]) #----> delete item in ab[effects] has negative in b[effects]  
    
    
    ab["effect"] = do_numeric_calculations(ab["effect"])  
    
    return ab   

  

   

  

#a = {'name': 'Lift-Load', 'parameters': ['?x - hoist', '?y - crate', '?z - surface', '?p - place', '?z1 - truck'], 'precondition': ['(at ?y ?p)', '(at ?x ?p)', '(clear ?y)', '(on ?y ?z)', '(at ?z1 ?p)', '(<= (+ (current_load ?z1) (weight ?y)) (load_limit ?z1))', '(available ?x)'],  

  

#     'effect': ['(not (lifting ?x ?y))', '(in ?y ?z1)', '(available ?x)', '(increase (current_load ?z1) (weight ?y))', '(not (at ?y ?p))', '(not (clear ?y))', '(clear ?z)', '(not (on ?y ?z))', '(increase (fuel-cost) 1)']}  

  

   

  

# a = {  

  

#       "name": "Unload",  

  

#       "parameters": ["?x - hoist", "?y - crate", "?z - truck", "?p - place"],  

  

#       "precondition": ["(at ?x ?p)", "(at ?z ?p)", "(available ?x)", "(in ?y ?z)"],  

  

#       "effect": ["(not (in ?y ?z))", "(not (available ?x))", "(lifting ?x ?y)", "(decrease (current_load ?z) (weight ?y))"]  

  

# }    

  

# b = {  



#      "name": "Drop",  



#       "parameters": ["?x - hoist", "?y - crate", "?z - surface", "?p - place"],  

  

#       "precondition": ["(at ?x ?p)", "(at ?z ?p)", "(clear ?z)", "(lifting ?x ?y)"],  

  

#       "effect": ["(available ?x)", "(not (lifting ?x ?y))", "(at ?y ?p)", "(not (clear ?z))", "(clear ?y)",   

#       "(on ?y ?z)"]  

  

# } 

  

  

a = { 

     "name": "build-sawmill", 

     "parameters": ["?p - place"], 

     "precondition": ["(>= (available timber ?p) 2)"], 

     "effect": ["(has-sawmill ?p)", "(increase (labour) 2)", "(decrease (available timber ?p) 2)"] 

} 

  

b= { 

     "name": "saw-wood", 

     "parameters": ["?p - place"], 

     "precondition": ["(has-sawmill ?p)", "(>= (available timber ?p) 1)"], 

     "effect": ["(decrease (available timber ?p) 1)", "(increase (available wood ?p) 1)"] 

} 

  

   

  

#b = {  

  

#          "name": "Drive",  

  

#          "parameters": ["?t - truck", "?p1 ?p2 - place"],  

  

#         "precondition": ["(at ?t ?p1)"],  

  

#          "effect": ["(not (at ?t ?p1))", "(at ?t ?p2)", "(increase (fuel-cost) 10)"]  

  

# }  

  

   

  

{  

  

    "name": "build-docks",  

  

    "parameters": ["?p - place"],  

  

    "precondition": ["(by-coast ?p)", "(>= (available wood ?p) 2)", "(>= (available stone ?p) 2)"],  

  

    "effect": ["(has-docks ?p)", "(increase (labour) 2)", "(decrease (available wood ?p) 2)", "(decrease (available stone ?p) 2)"]  

  

}  

  

   

  

   

  

{  

  

    "name": "build-wharf",  

  

    "parameters": ["?p - place"],  

  

    "precondition": ["(has-docks ?p)", "(>= (available iron ?p) 2)", "(>= (available stone ?p) 2)"],  

  

    "effect": ["(has-wharf ?p)", "(increase (labour) 2)", "(decrease (available iron ?p) 2)", "(decrease (available stone ?p) 2)"]  

  

}  

  

   

  

{'name': 'build-docks-build-wharf',   

  

'parameters': ['?p - place'],   

  

'precondition': ['(>= (available stone ?p) 2)', '(>= (available iron ?p) 2)', '(by-coast ?p)', '(>= (available wood ?p) 2)'],  

  

'effect': ['(has-wharf ?p)', '(decrease (available stone ?p) 4)', '(has-docks ?p)']}  

  

   

  

{'name': 'Lift-Load-Drive', 'parameters': ['?x - hoist', '?y - crate', '?z - surface', '?p1 ?p2 - place', '?z1 - truck'],   

  

'precondition': ['(available ?x)', '(on ?y ?z)', '(<= (+ (current_load ?z1) (weight ?y)) (load_limit ?z1))', '(at ?y ?p1)', '(clear ?y)', '(at ?z1 ?p1)', '(at ?x ?p1)'],  

  

'effect': ['(not (at ?z1 ?p1))', '(at ?z1 ?p2)', '(increase (fuel-cost) 11)', '(not (lifting ?x ?y))', '(in ?y ?z1)', '(available ?x)', '(increase (current_load ?z1) (weight ?y))', '(not (at ?y ?p1))', '(not (clear ?y))', '(clear ?z)', '(not (on ?y ?z))']}  

  

      

  

      

  

      

  

      

  

res = generate_macro_action(a,b)  


  

print(res)  

  


  

   

  

  

 

  # type: ignore