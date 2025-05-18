class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        result_dict = defaultdict()
        for _ in cpdomains:
            count, domains = _.split()
            count = int(count)
            sites = domains.split('.')

            for i in range(len(sites)):
                sites[i] = ".".join(sites[i:])

            for i in sites:
                if i in result_dict:
                    result_dict[i] += count
                else:
                    result_dict[i] = count
                    
        return [ str(result_dict[i]) + " " + i for i in result_dict]