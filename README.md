Workaround for https://youtrack.jetbrains.com/issue/TW-21447
## Usage
``` python
from TeamcityWebGui import TeamcityWebGui

teamcityGui = TeamcityWebGui("https://teamcity.example.com", user, password)
teamcityGui.moveBuildType('MyConfigurationId', 'ToMyProjectId')
```

### Requirements
- Firefox
- pypi modules in requirements.txt