Workaround for https://youtrack.jetbrains.com/issue/TW-21447
## Functional
1. Move Configuration to other Project
2. That's all for now :)
## Usage
``` python
from TeamcityWebGui import TeamcityWebGui

teamcityGui = TeamcityWebGui("https://teamcity.example.com", user, password)
teamcityGui.moveBuildType('MyConfigurationId', 'ToMyProjectId')
```

### Requirements
- Firefox
- pypi modules in requirements.txt
