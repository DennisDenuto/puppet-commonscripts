# This is a placeholder class.
#class bash_config_scripts($username) {
class common-scripts($username="") {
file { "/Users/$username/config":
    source  => "puppet:///modules/common-scripts/config",
    recurse => true,
    }
file { "/Users/$username/.gitconfig":
    source  => "puppet:///modules/common-scripts/git/.gitconfig",
    }
}
