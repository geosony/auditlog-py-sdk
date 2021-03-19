# Auditlog Python SDK

To write logs to AWS Kinesis stream

``` python

import auditlog
import json
auditlog.writer.kinesis_writer.write(json.dumps({"Hello": "Kinesis Writer"}))

```
