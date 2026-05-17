id - id is created when user creates a simulation. The db creates new data everytime a user does a new experiment
user_id - which user created the simulation
status - the status of the simulation the user is doing
simulation_type - is it a barnes hut or something else liek an algorithm you are implemeting
parameters - what are the values user has input
result_summary - the small summary of the simulation
result_artifact_path - something like if the user did a very big simulation it would get stored here
error_message - if the user has input wrong values. why the job failed
created_at - when the job was submitted
started_at - when the simulation actually started working
finished_at - done running and this is the finished condition

## simulation_jobs column types

id - UUID
user_id - UUID, nullable at first 
status - string/enum
simulation_type - string/enum
parameters - JSON
result_summary - JSON, nullable
result_artifact_path - string, nullable
error_message - string/text, nullable
created_at - datetime 
started_at - datetime, nullable
finished_at - datetime, nullable

## Job lifecycle

queued -> running
running -> completed
running -> failed
queued -> cancelled
running -> cancelled

completed -> running is not allowed
failed -> running is not allowed
cancelled -> running is not allowed