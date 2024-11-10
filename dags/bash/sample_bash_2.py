start = DummyOperator(dag=dag, task_id="start", *args, **kwargs)

t1 = BashOperator(
 task_id='ls1',
 bash_command='ls /tmp/downloaded',
 retries=3,
 dag=dag)

t2 = BashOperator(
 task_id='ls2',
 bash_command='ls /tmp/downloaded',
 dag=dag)

end = DummyOperator(dag=dag, task_id='end', *args, **kwargs)