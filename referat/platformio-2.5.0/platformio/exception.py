# Copyright 2014-2015 Ivan Kravets <me@ikravets.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


class PlatformioException(Exception):

    MESSAGE = None

    def __str__(self):  # pragma: no cover
        if self.MESSAGE:
            return self.MESSAGE % self.args
        else:
            return Exception.__str__(self)


class ReturnErrorCode(PlatformioException):
    pass


class MinitermException(PlatformioException):
    pass


class AbortedByUser(PlatformioException):

    MESSAGE = "Aborted by user"


class UnknownPlatform(PlatformioException):

    MESSAGE = "Unknown platform '%s'"


class PlatformNotInstalledYet(PlatformioException):

    MESSAGE = "The platform '%s' has not been installed yet. "\
        "Use `platformio platforms install` command"


class BoardNotDefined(PlatformioException):

    MESSAGE = "You need to specify board type using `-b` or `--board` "\
        "option. Supported boards list is available via "\
        " `platformio boards` command"


class UnknownBoard(PlatformioException):

    MESSAGE = "Unknown board type '%s'"


class UnknownFramework(PlatformioException):

    MESSAGE = "Unknown framework '%s'"


class UnknownPackage(PlatformioException):

    MESSAGE = "Detected unknown package '%s'"


class InvalidPackageVersion(PlatformioException):

    MESSAGE = "The package '%s' with version '%d' does not exist"


class NonSystemPackage(PlatformioException):

    MESSAGE = "The package '%s' is not available for your system '%s'"


class FDUnrecognizedStatusCode(PlatformioException):

    MESSAGE = "Got an unrecognized status code '%s' when downloaded %s"


class FDSizeMismatch(PlatformioException):

    MESSAGE = "The size (%d bytes) of downloaded file '%s' "\
        "is not equal to remote size (%d bytes)"


class FDSHASumMismatch(PlatformioException):

    MESSAGE = "The 'sha1' sum '%s' of downloaded file '%s' "\
        "is not equal to remote '%s'"


class NotPlatformProject(PlatformioException):

    MESSAGE = "Not a PlatformIO project. `platformio.ini` file has not been "\
        "found in current working directory (%s). To initialize new project "\
        "please use `platformio init` command"


class UndefinedEnvPlatform(PlatformioException):

    MESSAGE = "Please specify platform for '%s' environment"


class UnsupportedArchiveType(PlatformioException):

    MESSAGE = "Can not unpack file '%s'"


class ProjectEnvsNotAvailable(PlatformioException):

    MESSAGE = "Please setup environments in `platformio.ini` file"


class InvalidEnvName(PlatformioException):

    MESSAGE = "Invalid environment '%s'. The name must start with 'env:'"


class UnknownEnvNames(PlatformioException):

    MESSAGE = "Unknown environment names '%s'. Valid names are '%s'"


class CleanPioenvsDirError(PlatformioException):

    MESSAGE = "Can not remove temporary directory `%s`. "\
        "Please remove it manually"


class GetSerialPortsError(PlatformioException):

    MESSAGE = "No implementation for your platform ('%s') available"


class GetLatestVersionError(PlatformioException):

    MESSAGE = "Can not retrieve the latest PlatformIO version"


class APIRequestError(PlatformioException):

    MESSAGE = "[API] %s"


class LibAlreadyInstalled(PlatformioException):
    pass


class LibNotInstalled(PlatformioException):

    MESSAGE = "Library #%d has not been installed yet"


class LibInstallDependencyError(PlatformioException):

    MESSAGE = "Error has been occurred for library dependency '%s'"


class InvalidLibConfURL(PlatformioException):

    MESSAGE = "Invalid library config URL '%s'"


class BuildScriptNotFound(PlatformioException):

    MESSAGE = "Invalid path '%s' to build script"


class InvalidSettingName(PlatformioException):

    MESSAGE = "Invalid setting with the name '%s'"


class InvalidSettingValue(PlatformioException):

    MESSAGE = "Invalid value '%s' for the setting '%s'"


class CIBuildEnvsEmpty(PlatformioException):

    MESSAGE = "Can't find PlatformIO build environments.\n"\
        "Please specify `--board` or path to `platformio.ini` with "\
        "predefined environments using `--project-conf` option"


class SConsNotInstalledError(PlatformioException):

    MESSAGE = "The PlatformIO and `scons` aren't installed properly. "\
        "More details in FAQ/Troubleshooting section: "\
        "http://docs.platformio.org/en/latest/faq.html"


class UpgradeError(PlatformioException):

    MESSAGE = """%s

* Upgrade using `pip install -U platformio`
* Try different installation/upgrading steps:
  http://docs.platformio.org/en/latest/installation.html
"""


class CygwinEnvDetected(PlatformioException):

    MESSAGE = "PlatformIO does not work within Cygwin environment. "\
        "Use native Terminal instead."
