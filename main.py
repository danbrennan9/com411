
#import modules
import basics.decisions.nested_decision.nestception as decisions_nested_decision_nestception
import basics.decisions.nested_decision.nested as decisions_nested_decision_nested
import basics.decisions.simple_decision.comparison_operators as decisions_simple_decision_comparison_operators
import basics.decisions.simple_decision.counter as decisions_simple_decision_counter
import basics.decisions.simple_decision.if_elif_else as decisions_simple_decision_if_elif_else
import basics.decisions.simple_decision.if_else as decisions_simple_decision_if_elif
import basics.decisions.simple_decision.if_ as decisions_simple_decision_if
import basics.decisions.simple_decision.modulo_operator as decisions_simple_decision_modulo_operator
import basics.decisions.and_operator as decisions_and_operator
import basics.decisions.or_operator as decisions_or_operator
import basics.decisions.review as decisions_review
import basics.functions.ascii_character as functions_ascii_character
import basics.functions.ascii_code as functions_ascii_code
import basics.functions.function_calls as functions_function_calls
import basics.functions.function_with_loop as functions_function_with_loop
import basics.functions.function_with_nesting as functions_function_with_nesting
import basics.functions.function_with_parameter as functions_function_with_parameter
import basics.functions.function_with_parameters as functions_function_with_parameters
import basics.functions.multiple_functions as functions_multiple_functions
import basics.functions.return_values as functions_return_values
import basics.functions.simple_function as functions_simple_function
import basics.input.user_input as input_user_input
import basics.input.string_operators as input_string_operators
import basics.input.review as input_review
import basics.input.data_types as input_data_types
import basics.input.ascii_robot as input_ascii_robot
import basics.modules.guess_the_number as modules_guess_the_number
import basics.output.simple_message as output_simple_message
import basics.output.multiline_message as output_multiline_message
import basics.output.escape_characters as output_escape_characters
import basics.output.ascii_art as output_ascii_art
import basics.repetitions.for_loop.characters as repetitions_for_characters
import basics.repetitions.for_loop.count_down as repetitions_for_count_down
import basics.repetitions.for_loop.membership_operators as repetitions_for_membership_operators
import basics.repetitions.for_loop.range as repetitions_for_range
import basics.repetitions.for_loop.reverse as repetitions_for_reverse
import basics.repetitions.for_loop.simple as repetitions_for_simple
import basics.repetitions.nested_loop.nested as repetitions_nested_nested
import basics.repetitions.nested_loop.nesting as repetitions_nested_nesting
import basics.repetitions.while_loop.ascii as repetitions_while_ascii
import basics.repetitions.while_loop.count as repetitions_while_count
import basics.repetitions.while_loop.factorial as repetitions_while_factorial
import basics.repetitions.while_loop.len as repetitions_while_len
import basics.repetitions.while_loop.simple as repetitions_while_simple
import basics.repetitions.while_loop.sum_100 as repetitions_while_sum_100
import basics.repetitions.while_loop.sum_user_numbers as repetitions_while_sum_user_numbers

#function to run block a programs and call module runs
def run_block_a():
  print("Which program in 'Block A: Basics' do you wish to run?\n")
  response = input()

  if (response == "decisions_nested_decision_nestception"):
    decisions_nested_decision_nestception.run()

  elif (response == "decisions_nested_decision_nested"):
    decisions_nested_decision_nested.run()

  elif (response == "decisions_simple_decision_comparison_operators"):
    decisions_simple_decision_comparison_operators.run()

  elif (response == "decisions_simple_decision_counter"):
    decisions_simple_decision_counter.run()

  elif (response == "decisions_simple_decision_if_elif_else"):
    decisions_simple_decision_if_elif_else.run()

  elif (response == "decisions_simple_decision_if_else"):
    decisions_simple_decision_if_elif.run()

  elif (response == "decisions_simple_decision_if"):
    decisions_simple_decision_if.run()
  
  elif (response == "decisions_simple_decision_modulo_operator"):
    decisions_simple_decision_modulo_operator.run()

  elif (response == "decisions_and_operator"):
    decisions_and_operator.run()

  elif (response == "decisions_or_operator"):
    decisions_or_operator.run()
  
  elif (response == "decisions_review"):
    decisions_review.run()

  elif (response == "functions_ascii_character"):
    functions_ascii_character.run()

  elif (response == "functions_ascii_code"):
    functions_ascii_code.run()

  elif (response == "functions_function_calls"):
    functions_function_calls.run()

  elif (response == "functions_function_with_loop"):
    functions_function_with_loop.run()

  elif (response == "functions_function_with_nesting"):
    functions_function_with_nesting.run()

  elif (response == "functions_function_with_parameter"):
    functions_function_with_parameter.run()

  elif (response == "functions_function_with_parameters"):
    functions_function_with_parameters.run()

  elif (response == "functions_multiple_functions"):
    functions_multiple_functions.run()

  elif (response == "functions_return_values"):
    functions_return_values.run()

  elif (response == "functions_simple_function"):
    functions_simple_function.run()

  elif (response == "input_user_input"):
    input_user_input.run()

  elif (response == "input_string_operators"):
    input_string_operators.run()

  elif (response == "input_review"):
    input_review.run()

  elif (response == "input_data_types"):
    input_data_types.run()

  elif (response == "input_ascii_robot"):
    input_ascii_robot.run()

  elif (response == "modules_guess_the_number"):
    modules_guess_the_number.run()

  elif (response == "output_simple_message"):
    output_simple_message.run()

  elif (response == "output_multiline_message"):
    output_multiline_message.run()

  elif (response == "output_escape_characters"):
    output_escape_characters.run()

  elif (response == "output_ascii_art"):
    output_ascii_art.run()

  elif (response == "repetitions_for_characters"):
    repetitions_for_characters.run()

  elif (response == "repetitions_for_count_down"):
    repetitions_for_count_down.run()

  elif (response == "repetitions_for_membership_operators"):
    repetitions_for_membership_operators.run()

  elif (response == "repetitions_for_range"):
    repetitions_for_range.run()

  elif (response == "repetitions_for_reverse"):
    repetitions_for_reverse.run()

  elif (response == "repetitions_for_simple"):
    repetitions_for_simple.run()

  elif (response == "repetitions_nested_nested"):
    repetitions_nested_nested.run()

  elif (response == "repetitions_nested_nesting"):
    repetitions_nested_nesting.run()

  elif (response == "repetitions_while_ascii"):
    repetitions_while_ascii.run()
  
  elif (response == "repetitions_while_count"):
    repetitions_while_count.run()

  elif (response == "repetitions_while_factorial"):
    repetitions_while_factorial.run()

  elif (response == "repetitions_while_len"):
    repetitions_while_len.run()

  elif (response == "repetitions_while_simple"):
    repetitions_while_simple.run()
  
  elif (response == "repetitions_while_sum_100"):
    repetitions_while_sum_100

  elif (response == "repetitions_while_sum_user_numbers"):
    repetitions_while_sum_user_numbers

  elif (response == "functions_function_calls"):
    functions_function_calls.run()
    
  else:
    print("I don't understand what you mean.")

#interface
def run():
  is_running = True

  while(is_running):
    print("""
    What would you like to do?
    [a] Run 'Block A: Basic programs'
    [b] Quit
    \n""")
    response = input()

    if (response == "a"):
      run_block_a()

    elif (response == "b"):
      break

    else:
      print("Invalid option! Please try again.")
      
run()