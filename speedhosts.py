import re
import shutil


def get_mapping():
    v4 = re.compile('(?:\d{1,3}\.){3}\d{1,3}')
    v6 = re.compile('^(^(([0-9A-F]{1,4}(((:[0-9A-F]{1,4}){5}::[0-9A-F]{1,4})|((:[0-9A-F]{1,4}){4}::[0-9A-F]{1,4}(:[0-9A-F]{1,4}){0,1})|((:[0-9A-F]{1,4}){3}::[0-9A-F]{1,4}(:[0-9A-F]{1,4}){0,2})|((:[0-9A-F]{1,4}){2}::[0-9A-F]{1,4}(:[0-9A-F]{1,4}){0,3})|(:[0-9A-F]{1,4}::[0-9A-F]{1,4}(:[0-9A-F]{1,4}){0,4})|(::[0-9A-F]{1,4}(:[0-9A-F]{1,4}){0,5})|(:[0-9A-F]{1,4}){7}))$|^(::[0-9A-F]{1,4}(:[0-9A-F]{1,4}){0,6})$)|^::$)|^((([0-9A-F]{1,4}(((:[0-9A-F]{1,4}){3}::([0-9A-F]{1,4}){1})|((:[0-9A-F]{1,4}){2}::[0-9A-F]{1,4}(:[0-9A-F]{1,4}){0,1})|((:[0-9A-F]{1,4}){1}::[0-9A-F]{1,4}(:[0-9A-F]{1,4}){0,2})|(::[0-9A-F]{1,4}(:[0-9A-F]{1,4}){0,3})|((:[0-9A-F]{1,4}){0,5})))|([:]{2}[0-9A-F]{1,4}(:[0-9A-F]{1,4}){0,4})):|::)((25[0-5]|2[0-4][0-9]|[0-1]?[0-9]{0,2})\.){3}(25[0-5]|2[0-4][0-9]|[0-1]?[0-9]{0,2})$$')

    ip_to_host = {}

    with open('/etc/hosts', 'r') as hostsf:
        for line in hostsf:
            line = line.replace('\t', ' ')
            parts = line.split(' ')
            ip = parts[0].strip()
            if v4.match(ip) or v6.match(ip):
                hostnames_without_comment = ' '.join(parts[1:])
                if '#' in line:
                    hostnames_without_comment = hostnames_without_comment.split('#')[0]
                hostnames = [h.strip() for h in hostnames_without_comment.split(' ') if h]

                if not ip in ip_to_host:
                    ip_to_host[ip] = hostnames
                else:
                    ip_to_host[ip].extend(hostnames)
                # Remove duplicates
                ip_to_host[ip] = list(set(ip_to_host[ip]))

    return ip_to_host


def write_mapping(mapping):
    shutil.copy('/etc/hosts', '/etc/hosts.bak')
    with open('/etc/hosts', 'w') as hostsf:
        for ip, hosts in mapping.iteritems():
            hostsf.write('%s %s\n' % (ip, ' '.join(hosts)))


if __name__ == '__main__':
    write_mapping(get_mapping())
