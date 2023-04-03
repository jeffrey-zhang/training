# get all contributors from a repo
# Usage: get_all_contributors_from_repo.sh <repo>

#  获取nebulagrah repo 的所有contributors, 和贡献数
curl -s https://api.github.com/repos/nebulagraph/$1/contributors | jq -r '.[] | [.login, .contributions] | @tsv'